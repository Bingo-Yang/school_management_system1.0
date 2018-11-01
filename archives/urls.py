#coding=utf-8
from django.conf.urls import url

from archives import views

urlpatterns = [
    url(r'^student/',views.stu_info_view,name='student'),
    url(r'^register/',views.stu_school_register,name='register'),
    url(r'^maintenance/(\d?)',views.stu_info_maintenance,name='maintenance'),
    url(r'^query/',views.stu_register_query,name='query'),
    url(r'^teacher/(\d?)',views.tea_info_view,name='teacher'),
    url(r'^teaMaintenance/',views.tea_info_maintenance,name='teaMaintenance'),

]