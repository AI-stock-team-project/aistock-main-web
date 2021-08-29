from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('optimize/max_sharpe/', views.build_portfolio, {'optimize_method':'max_sharpe'}, name='max_sharpe'),
    path('optimize/efficient/', views.build_portfolio, {'optimize_method':'efficient'}, name='efficient'),
    path('optimize/report/', views.build_portfolio_report, name='report'),
    path('optimize/report_demo/', views.test_report, name='report_demo'),
]
