from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # board
    path('<route_id>/', views.index, name='index'),
    # path('discussion/', views.index, {'board_id':1}),
    # path('', views.index),
    path('<route_id>/<int:post_id>/', views.view, name='view'),
    path('<route_id>/write/', views.write, name='write'),
    path('<route_id>/store/', views.post_store, name='store'),
    path('<route_id>/edit/', views.edit, name='edit'),
    path('<route_id>/update/', views.update, name='update'),
    path('<route_id>/delete/', views.delete, name='delete'),
    path('<route_id>/reply/', views.reply, name='reply'),
    path('<route_id>/reply_store/', views.reply_store, name='reply_store'),
]