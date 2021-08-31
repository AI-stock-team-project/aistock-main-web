from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
import requests
from mypage.models import UserStockPinned


@login_required()
def index(request):
    """
    LSTM
    """
    # 관심 종목 조회

    main_list = UserStockPinned.objects.filter(
        user_id=request.user.id,
        is_active=True
    ).all()

    context = {
        'main_list': main_list
    }
    return render(request, 'lstm/index.html', context)


def predict_close_price_report(request):
    stock_symbol = request.POST.get('stock_symbol')

    if len(stock_symbol) < 2:
        messages.error(request, '잘못된 접근입니다.')
        return redirect('lstm:index')

    # ######## api 통신 ########
    url = f'http://{settings.DATA_API_URL}/lstm/predict_close_price/{stock_symbol}'

    start_date = '2018-01-01'
    # api 파라미터
    params = {
        'start_date': start_date,
    }
    response = requests.post(url, data=params)

    json_data = json.loads(response.text)

    predicted_close_price = json_data.get('predict_close_price')
    graph_url = json_data.get('graph_url')

    context = {
        'predicted_close_price': predicted_close_price,
        'stock_symbol': stock_symbol,
        'graph_url': graph_url
    }
    return render(request, 'lstm/report.html', context)


def report_demo(request):
    """
    결과 화면을 테스트하기 위한 용도
    """
    return render(request, 'lstm/report.html', {
        'predicted_close_price': '20729',
        'stock_symbol': '006840',
        'graph_url': '/static/return_lstm_20210901_041830.png'
    })
