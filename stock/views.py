from django.shortcuts import render
from .models import Stock, StockPrice
from django.core.paginator import Paginator

def index(request):
    """
    종목 조회
    """

    # 페이지 변수
    page = int(request.GET.get('page', '1'))
    # 목록에서 표현되는 게시글 수 
    per_page = 20

    results = Stock.objects.all()
    paginator = Paginator(results, per_page=per_page)
    main_list = paginator.get_page(page)

    context = {
        'main_list': main_list
    }
    return render(request, 'stock/list.html', context)
