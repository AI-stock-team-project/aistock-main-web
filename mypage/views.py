from django.shortcuts import render

# Create your views here.
def index(request):
    """
    메인 페이지
    """
    return render(request, 'mypage/index.html')