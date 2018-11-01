# coding=utf-8
from django.conf.urls import url

from teacher import views

urlpatterns=[
    url(r'^$',views.teacher_view),
    url(r'^show/',views.showtea_view),
    #班主任
    url(r'^guide/',views.guide_view),
    #任课老师
    url(r'^coursetea/',views.coursetea_view),
    #班主任班级
    url(r'^showguide/',views.showguide_view),
    #班主任信息
    url(r'^showguide2/',views.showguide2_view),
    #查询任课老师
    url(r'^querytea/',views.querycoursetea_view),

]