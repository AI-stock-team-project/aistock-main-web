from django.shortcuts import render
from stock.models import Stock, StockPrice
from django.db.models import Subquery
from django.db.models.expressions import OuterRef
from strategy.models import StrategyStockList
from django.http import JsonResponse
from django.core import serializers


def index(request):
    """
    메인 페이지
    """
    return render(request, 'main/index.html')


def ajax_strategy_stock_top_index(request):
    mo_1 = get_strategy_stocks('mo_1')
    mo_3 = get_strategy_stocks('mo_3')
    dual_mo = get_strategy_stocks('dual_mo')
    soaring = get_strategy_stocks('soaring')
    up_freq = get_strategy_stocks('up_freq')

    return JsonResponse({
        'mo_1' : mo_1,
        'mo_3' : mo_3,
        'dual_mo' : dual_mo,
        'soaring' : soaring,
        'up_freq' : up_freq,
    },  safe=False)


def get_strategy_stocks(type_code):
    strategy_types = {
        'mo_1': 'mo_1',
        'mo_3': 'mo_3',
        'dual_mo': 'dual_mo',
        'soaring': 'soaring',
        'up_freq': 'up_freq',
    }
    strategy_type = strategy_types[type_code]
    qs = get_strategy_stocks_queryset(strategy_type)

    result=[]
    for item in qs.all():
        result.append({'ticker':item.ticker, 'name': item.name})
    
    return result


def get_strategy_stocks_queryset(strategy_type):

    
    # 전략별 종목 조회
    strategy_stocks = StrategyStockList.objects.filter(
        strategy_code=strategy_type
    ).annotate(
        name=Subquery(
            Stock.objects.filter(code=OuterRef('ticker')).values('name')[:1]
        ),
        market=Subquery(
            Stock.objects.filter(code=OuterRef('ticker')).values('market')[:1]
        )
    ).order_by('rank', 'name')[:10]

    return strategy_stocks


def test(request):
    """
    메인 페이지
    """
    return render(request, 'main/test.html')
