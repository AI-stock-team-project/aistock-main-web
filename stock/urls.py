from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.index, name='index'),
    path('toggle_stock_pinned/activate/<stock_symbol>/', views.toggle_stock_pinned, {'mode': 'activate'},
         name='toggle_stock_pinned_activate'),
    path('toggle_stock_pinned/deactivate/<stock_symbol>/', views.toggle_stock_pinned, {'mode': 'deactivate'},
         name='toggle_stock_pinned_activate'),
]
