from django.shortcuts import render


# Create your views here.
def index(request):
    """
    전략별
    """
    return render(request, 'strategy/index.html')
