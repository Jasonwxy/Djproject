"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path  # 路由模式
from django.urls import re_path  # 正则表达式模式
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('current_time/', views.current_time),
    path('', views.index),
    path('get_names/', views.get_names),
    re_path('hello/', views.hello),
    re_path('^test/([0-9]{1,2})/$', views.test),  # 正则表达式用括号括起，表示将匹配到的值作为参数传递给views.text()方法
    path('notice/', views.notice),
    path('display_meta/', views.display_meta),
    path('search_form/', views.search_form),
    path('search_result/', views.search_result)
]
