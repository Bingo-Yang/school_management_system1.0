# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from login.models import *
#编辑admin后台类
class BlogArticleAdmin(admin.ModelAdmin):
    #显示表格列表字段
    list_display = ('stu_id','stu_name','stu_age',)
    #条件查询字段
    list_filter = ('clazz',)
    # 搜索框中根据某些字段进行查询(优先选择字段1)
    search_fields = ('stu_name',)
admin.site.register(User)
admin.site.register(TeachingStaff)
admin.site.register(StuScore)
admin.site.register(StuRegister)
admin.site.register(HeadTeacher)
admin.site.register(Teacher)
admin.site.register(BookBorrow)
admin.site.register(Stu,BlogArticleAdmin)
admin.site.register(Clazz)
admin.site.register(Major)
admin.site.register(Grade)
admin.site.register(Book)
admin.site.register(Course)