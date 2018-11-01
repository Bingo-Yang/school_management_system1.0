# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.models import User


# 用户维护
def append(request):
    if request.method == 'GET':
        return render(request, 'append.html')
    else:
        try:
            user_id = request.POST.get('user_id', '')
            user_id = int(user_id)
            user_name = request.POST.get('user_name', '')
            user_password = request.POST.get('user_password', '')
            user_nickname = request.POST.get('user_nickname', '')
            if user_password == user_nickname:
                User.objects.create(user_id=user_id, user_name=user_name, user_password=user_password,
                                    user_nickname=user_nickname)
                return HttpResponse('<script>alert("注册成功!");location.href="/users/append/";</script>')
        except:
            return HttpResponse('<script>alert("注册失败!");location.href="/users/append/";</script>')

# 用户查询
def demand(request, num):
    if request.method == 'GET':
        if not num:
            return render(request, 'demand.html')
        else:
            User.objects.filter(user_id=num).delete()
            return HttpResponse('删除成功')
    else:
        try:
            demand = request.POST.get('demand', '')
            query = request.POST.get('query', '')
            if demand == '用户名':
                users = User.objects.filter(user_name=query)
                return render(request, 'demand.html', {'users': users})
            elif demand == '用户编号':
                users = User.objects.filter(user_id=query)
                return render(request, 'demand.html', {'users': users})
            elif demand == '所有用户':
                users = User.objects.all()
                return render(request, 'demand.html', {'users': users})
        except:
            return HttpResponse('<script>alert("请输入编号!");location.href="/users/demand/";</script>')

