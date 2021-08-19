from django.shortcuts import render


# Create your views here.
def index(request):
    """
    LSTM
    """
    return render(request, 'lstm/index.html')
