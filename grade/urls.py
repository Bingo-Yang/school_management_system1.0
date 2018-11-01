#coding=utf-8
from django.conf.urls import url

from grade import views

urlpatterns = [
    #成绩录入
    url(r'^grade_register/',views.grade_register_view),
    #成绩查询
    url(r'^grade_query/', views.grade_query_view),
    #班级成绩统计
    url(r'^grade_claz/', views.grade_claz_view),
    #年级成绩统计
    url(r'^grade_clazz/', views.grade_clazz_view),
]