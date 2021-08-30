from django.shortcuts import render
from .models import Stock, StockPrice
from django.core.paginator import Paginator
from mypage.models import UserStockPinned
from django.http import HttpResponse, JsonResponse
from django.db.models.expressions import OuterRef
from django.db.models import Subquery

def index(request):
    """
    종목 조회
    """

    # 페이지 변수
    page = int(request.GET.get('page', '1'))
    # 목록에서 표현되는 게시글 수 
    per_page = 20

    results = Stock.objects.all()

    if request.user.is_active:
        # 로그인된 상태에서는, 관심 종목 여부를 같이 조회한다.
        # price_qs = StockPrice.objects.filter(code=OuterRef('ticker')).order_by('-date')
        pinned_qs = UserStockPinned.objects.filter(stock_id = OuterRef('id'), user_id = request.user.id)
        results = results.annotate(
            pinned = Subquery(
                pinned_qs.values('is_active')[:1]
            )
        )
    
    paginator = Paginator(results, per_page=per_page)
    main_list = paginator.get_page(page)

    context = {
        'main_list': main_list
    }
    return render(request, 'stock/list.html', context)


def toggle_stock_pinned(request, stock_id, mode):
    """
    관심 종목 추가/제거의 토글을 한 경우
    """
    # 유저 인증 여부 체크.
    if not request.user.is_active:
        return JsonResponse({
            'message' : 'failed',
            'mode': mode
        })

    msg = ''

    stock_pinned_qs = UserStockPinned.objects.filter(
        stock_id = stock_id,
        user_id = request.user.id
    )
    if mode == 'activate':
        # 활성화.
        if stock_pinned_qs.exists():
            # 값이 있었을 경우에 is_active 를 변경
            stock_pinned = stock_pinned_qs.get()
            if not stock_pinned.is_active:
                stock_pinned.is_active = True
                stock_pinned.save()

        else:
            # 신규 추가.
            stock = Stock.objects.get(id=stock_id)

            # 추가 처리
            stock_pinned = UserStockPinned()
            stock_pinned.stock = stock
            stock_pinned.user = request.user
            stock_pinned.save()

    else:
        # 비활성화
        # stock_pinned = UserStockPinned.objects.get(stock_id = stock_id, user_id = user_id)
        if stock_pinned_qs.exists():
            stock_pinned = stock_pinned_qs.get()
            if stock_pinned.is_active:
                stock_pinned.is_active = False
                stock_pinned.save()
        else:
            return JsonResponse({
                'message' : 'success',
                'mode': mode
            })

    # 데이터 얻기
    # pinned_stock = UserStockPinned.objects.get(id=stock_id)
    # if pinned_stock is None:
    #     # 신규 생성
    #     msg = '값이 없음'
    # else: 
    #     msg = f'값이 있음 {pinned_stock}'

    return JsonResponse({
        'message' : msg,
        'mode': mode
    }, json_dumps_params = {'ensure_ascii': True})
