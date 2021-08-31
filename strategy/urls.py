from django.urls import path
from . import views

app_name = 'strategy'
urlpatterns = [
    path('', views.index, name='index'),
    path('momentum_1month/', views.index, {'p_type': 'mo_1'}, name='mo_1'),
    path('momentum_3months/', views.index, {'p_type': 'mo_3'}, name='mo_3'),
    path('dual_momentum/', views.index, {'p_type': 'dual_mo'}, name='dual_mo'),
    path('soaring/', views.index, {'p_type': 'soaring'}, name='soaring'),
    path('up_frequency/', views.index, {'p_type': 'up_freq'}, name='up_freq'),
]
