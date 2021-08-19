from django.shortcuts import render
from .models import Stock, StockPrice
from django.core.paginator import Paginator

def index(request):
    """
    종목 조회
    """
    results = Stock.objects.all()
    paginator = Paginator(results, per_page=10)
    main_list = paginator.get_page(1)


    context = {
        'main_list': main_list
    }
    return render(request, 'stock/list.html', context)
