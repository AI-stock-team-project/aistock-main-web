from django.shortcuts import render
from mypage.models import UserStockPinned
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    """
    마이페이지
    """
    return render(request, 'mypage/index.html')


@login_required()
def pinned_stock(request):
    # 유저 인증 여부 체크.
    if not request.user.is_active:
        return 

    # 페이지 변수
    page = int(request.GET.get('page', '1'))
    # 목록에서 표현되는 게시글 수 
    per_page = 30

    stock_pinned_qs = UserStockPinned.objects.filter(
        user_id = request.user.id,
        is_active = True
    )

    paginator = Paginator(stock_pinned_qs, per_page=per_page)
    main_list = paginator.get_page(page)

    context = {
        'main_list': main_list
    }
    return render(request, 'mypage/pinned_list.html', context)