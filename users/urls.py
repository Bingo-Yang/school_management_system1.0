# coding=utf-8
from django.conf.urls import url
from .import views
urlpatterns = [
    # 用户维护
    url(r'^append/',views.append),
    # 用户查询
    url(r'^demand/(\d?)', views.demand)
]