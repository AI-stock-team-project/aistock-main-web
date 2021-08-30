from django.urls import path
from . import views

app_name = 'mypage'
urlpatterns = [
    path('', views.index, name='index'),
    path('pinned_stock/', views.pinned_stock, name='pinned_stock'),
]
