from django.db.models.expressions import OuterRef
# import strategy
from django.shortcuts import render
from stock.models import Stock, StockPrice
from .models import StrategyStockList
# from django.core.paginator import Paginator
from django.db.models import Subquery
from mypage.models import UserStockPinned


# Create your views here.
def index(request, p_type='mo_1'):
    """
    전략별 종목 리스트
    """

    strategy_types = {
        'mo_1': 'mo_1',
        'mo_3': 'mo_3',
        'dual_mo': 'dual_mo',
        'soaring': 'soaring',
        'up_freq': 'up_freq',
    }
    strategy_type = strategy_types[p_type]
    
    # prices 정보를 가져오기 위한 쿼리셋. 서브쿼리로 이용
    price_qs = StockPrice.objects.filter(code=OuterRef('ticker')).order_by('-date')

    strategy_stocks = StrategyStockList.objects.filter(
        strategy_code=strategy_type
    ).all().annotate(
        name=Subquery(
            Stock.objects.filter(code=OuterRef('ticker')).values('name')[:1]
        ),
        ticker_id=Subquery(
            Stock.objects.filter(code=OuterRef('ticker')).values('id')[:1]
        ),
        market=Subquery(
            Stock.objects.filter(code=OuterRef('ticker')).values('market')[:1]
        ),
        close=Subquery(
            price_qs.values('close')[:1]
        )
    ).order_by('rank', 'name')
    
    if request.user.is_active:
        pinned_qs = UserStockPinned.objects.filter(stock_id=OuterRef('ticker_id'), user_id=request.user.id)
        strategy_stocks = strategy_stocks.annotate(
            pinned=Subquery(
                pinned_qs.values('is_active')[:1]
            )
        )

    # 랭킹 사용 유무
    if p_type == 'mo_1' or p_type == 'mo_3' or p_type == 'up_freq':
        is_rank_enabled = True
    else:
        is_rank_enabled = False

    context = {
        'strategy_type': p_type,
        'is_rank_enabled': is_rank_enabled,
        'main_list': strategy_stocks
    }

    return render(request, 'strategy/index.html', context)
