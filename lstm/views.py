from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
import json
import requests

# Create your views here.
def index(request):
    """
    LSTM
    """
    return render(request, 'lstm/index.html')


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

    context = {
        'predicted_close_price': predicted_close_price,
        'stock_symbol': stock_symbol
    }
    return render(request, 'lstm/report.html', context)
