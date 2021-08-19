from django.shortcuts import render


def index(request):
    """
    마이페이지
    """
    return render(request, 'mypage/index.html')
