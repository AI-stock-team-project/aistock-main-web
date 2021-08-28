from django.shortcuts import render


def index(request):
    """
    포트폴리오
    """
    return render(request, 'portfolio/index.html')


def step1(request, optimize_method):
    page_id = request.GET.get('page', 'choice_years')
    if page_id == 'choice_years':
        return render(request, 'portfolio/choice_years.html')
    elif page_id == 'choice_money':
        return render(request, 'portfolio/choice_money.html')
    elif page_id == 'choice_risk':
        return render(request, 'portfolio/choice_risk.html')
    elif page_id == 'choice_items':
        return render(request, 'portfolio/choice_items.html')


    return render(request, 'portfolio/choice_years.html')

