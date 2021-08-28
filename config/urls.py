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
import mypage.views
import lstm.views
# import portfolio.views
# import strategy.views

urlpatterns = [
    path('', main.views.index),
    path('test/', main.views.test),
    # path('stock/', stock.views.index),
    path('stock/', include('stock.urls')),
    path('mypage/', mypage.views.index),
    # path('portfolio/', portfolio.views.index),
    path('portfolio/', include('portfolio.urls')),
    path('lstm/', lstm.views.index),
    path('strategy/', include('strategy.urls')),
    path('board/', include('board.urls')),
    # path('news/', mypage.views.index),
    # admin, accounts
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
