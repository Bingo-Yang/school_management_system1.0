# coding=utf-8
"""school_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #用户登录 数据库
    url(r'^', include('login.urls')),
    #教职工
    url(r'^teach/', include('teacher.urls')),
    url(r'^login/', include('login.urls')),
    #档案管理
    url(r'^archive/', include('archives.urls')),
    # 图书管理
    url(r'^book/', include('book.urls')),
    # 成绩管理
    url(r'^grade/', include('grade.urls')),
    # 用户管理
    url(r'^users/', include('users.urls')),
    # 代码维护
    url(r'^maintenance/', include('maintenance.urls')),
]
