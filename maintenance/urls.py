# coding=utf-8
from django.conf.urls import url
from .import views
urlpatterns = [
    # 代码维护
    url(r'^maintain/',views.maintain),
    # 修改
    url(r'^change/(\d+)/(\D+)/(\d{1})', views.change),
    # 年级维护
    url(r'^grade/', views.grade),
    url(r'^change1/(\d+)/(\D+)/(\d{1})',views.change1),
    # 班级维护
    url(r'^clazz/', views.clazz),
    url(r'^change2/(\d+)/(.+)/(.+)/(.+)/(\d{1})',views.change2),
    # 学科维护
    url(r'^course/',views.course),
    url(r'^change3/(\d+)/(\D+)/(\d{1})',views.change3),

]