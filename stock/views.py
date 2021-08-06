from django.shortcuts import render


def index(request):
    """
    종목 조회
    """
    return render(request, 'stock/list.html')
