# import portfolio
from django.shortcuts import render
import requests
# from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import json
from math import isnan


def index(request):
    """
    포트폴리오
    """
    return render(request, 'portfolio/index.html')


def build_portfolio(request, optimize_method='max_sharpe'):

    context = {
        'optimize_method': optimize_method
    }
    return render(request, 'portfolio/choice.html', context)


def build_portfolio_report(request):
    years = int(request.POST.get('years'))
    money = request.POST.get('money')
    risk = int(request.POST.get('risk')) * 0.01
    # assets = request.POST.get('assets')
    optimize_method = request.POST.get('optimize_method')
    asset_method = request.POST.get('asset_method', 'custom')

    for key, value in request.POST.items():
        print(f'Key: {key}')
        print(f'Value: {value}')

    # return HttpResponse(f'TEST {asset_method}')

    # url 생성을 위한 optimize_method 선택
    opt_method_uri_codes = {
        'max_sharpe': 'maxsharpe',
        'efficient': 'efficient',
    }
    opt_method_uri = opt_method_uri_codes[optimize_method]

    # url 생성을 위한 asset_method 선택
    asset_method_uri_codes = {
        'custom': 'custom',
        'dual_momentum': 'dual_momentum',
        'momentum_1month': 'momentum_1month',
        'momentum_3month': 'momentum_3month',
        'soaring': 'soaring',
        'up_freq': 'up_freq',
    }
    asset_method_uri = asset_method_uri_codes[asset_method]

    # ######## api 통신 ########
    # api url 생성
    # url = f'http://localhost:15000/portfolio/{opt_method_uri}/{asset_method_uri}'
    # url = f'http://data-api:5000/portfolio/{opt_method_uri}/{asset_method_uri}'
    url = f'http://{settings.DATA_API_URL}/portfolio/{opt_method_uri}/{asset_method_uri}'
    
    # api 파라미터
    params = {
        'years': years,
        'money': money,
        'risk_limit': risk,
        'assets': ['005930', '000660', '035720', '035420', '051910']
    }
    response = requests.post(url, data=params)

    # r_json = response.json()
    # res_json = json.loads(response)
    json_data = json.loads(response.text)

    # return HttpResponse(f'TEST {r_json}')
    portfolio = json_data.get('result_df')
    report = json_data.get('result')

    for item in portfolio:
        if str(item['name']).lower() == 'nan':
            item['name'] = '합계'
    
    v_parameters = {
        'years': years,
        'money': money,
        'optimize_method': optimize_method,
        'risk': risk
    }
    context = {
        'params': v_parameters,
        'report': report,
        'portfolio': portfolio,
    }
    return render(request, 'portfolio/report.html', context)


def test_report(request):
    portfolio = [
        {'name': 'NAVER', 'symbol': '035420', 'number': 30.0, 'money': 12600000.0, 'weight': 0.8431872477966714}, 
        {'name': '삼성전자', 'symbol': '005930', 'number': 21.0, 'money': 1560300.0, 'weight': 0.10441468751882114}, 
        {'name': 'LG화학', 'symbol': '051910', 'number': 1.0, 'money': 783000.0, 'weight': 0.05239806468450744}, 
        {'name': '합계', 'symbol': 'NaN', 'number': 52.0, 'money': 14943300.0, 'weight': 1.0}
    ]

    report = {
        'expected_annual_return': 0.123456789123456789,
        'annual_volatility': 0.123456789123456789,
        'sharpe_ratio': 10.123456789123456789,
        'balance': 9450.123456789123456789,
        'trends_file_url': '/static/_return_trends_sample.png',
        'votality_file_url': '/static/_votality_trends_sample.png'
    }

    v_parameters = {
        'years': 1,
        'money': 15000000,
        'optimize_method': 'efficient',
        'risk': '0.3'
    }

    context = {
        'params': v_parameters,
        'report': report,
        'portfolio': portfolio,

    }
    return render(request, 'portfolio/report.html', context)
