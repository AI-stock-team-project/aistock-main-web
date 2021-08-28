from django.shortcuts import render


def index(request):
    """
    포트폴리오
    """
    return render(request, 'portfolio/index.html')


def step1(request, optimize_method='max_sharpe'):

    context = {
        'optimize_method': optimize_method
    }
    return render(request, 'portfolio/choice_years.html', context)

