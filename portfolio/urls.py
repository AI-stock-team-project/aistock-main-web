from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('optimize/max_sharpe/', views.step1, {'optimize_method':'max_sharpe'}, name='max_sharpe'),
    path('optimize/efficient/', views.step1, {'optimize_method':'efficient'}, name='efficient'),
    path('optimize/result/', views.index, name='result'),
]
