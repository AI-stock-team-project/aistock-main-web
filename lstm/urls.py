from django.urls import path
from . import views

app_name = 'lstm'
urlpatterns = [
    path('', views.index, name='index'),
    # path('pinned_stock/', views.pinned_stock, name='pinned_stock'),
    path('predict_close_price/', views.predict_close_price_report, name='predict_close_price'),
    path('predict_close_price_demo/', views.report_demo, name='predict_close_price_demo'),
]
