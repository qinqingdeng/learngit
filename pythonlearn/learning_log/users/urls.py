"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
'''定义users的URL模式'''
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登陆界面
    path('login/', LoginView.as_view(),
        name='login'),
    #zhuxiao
    path('logout/',LogoutView.as_view(),name='logout'),
    # 注册页面
    path('register/',views.register,name='register'),
]
app_name='users'
