"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import main.views
import stock.views
import mypage.views
import lstm.views
import news.views
import board.views
import portfolio.views
import strategy.views

urlpatterns = [
    path('', main.views.index),
    path('test/', main.views.test),
    path('stock/', stock.views.index),
    path('mypage/', mypage.views.index),
    path('portfolio/', portfolio.views.index),
    path('lstm/', lstm.views.index),
    path('strategy/', strategy.views.index),
    # path('news/', mypage.views.index),
    # board
    path('board/', board.views.index),
    path('board/view/', board.views.view),
    path('board/writeform/', board.views.writeform),
    path('board/write', board.views.write),
    path('board/updateform/', board.views.updateform),
    path('board/update', board.views.update),
    path('board/delete/', board.views.delete),
    path('board/replyform/', board.views.replyform),
    path('board/reply', board.views.reply),
    # admin, accounts
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
