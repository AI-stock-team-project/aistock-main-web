from django.shortcuts import render


def index(request):
    """
    메인 페이지
    """
    return render(request, 'main/index.html')


def test(request):
    """
    메인 페이지
    """
    return render(request, 'main/test.html')
