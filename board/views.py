from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Board
    """
    return render(request, 'board/index.html')