from django.shortcuts import render


def index(request):
    """
    포트폴리오
    """
    return render(request, 'portfolio/index.html')