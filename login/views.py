# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from login.models import User


def login_view(request):
    # return HttpResponse('123')
    if request.method == 'GET':
        if request.COOKIES.has_key('login'):
            login = request.get_signed_cookie('login', salt='hello').split(',')
            uname = login[0]
            pwd =  login[1]
            remember = login[2]

            return render(request, 'login.html', {'uname': uname, 'pwd': pwd, 'remember': remember,})
        return render(request, 'login.html')
    #获取用户数据
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        remember = request.POST.get('remember', '')
        # 用cookie记住用户名、密码
        if remember == 'on':
            remember = '1'
        else:
            remember = '0'
        response = HttpResponse()
        # 遍历用户数据库匹配
        if uname and pwd:
            users = User.objects.filter(user_name=uname,user_password=pwd)
            if users:
                #登陆成功用session记住用户
                for use in users:
                    request.session['uname'] = uname
                    request.session.set_expiry(60 * 60 * 24 * 3)
                    # return HttpResponse('<script>alert("登录成功");location.href="/login/index/";</script>')
                    return  redirect('/login/index/')
            if remember == '1':
                response.set_signed_cookie('login',uname+','+pwd+','+remember,salt='hello',
                                           path='/login/', max_age=72 * 60 * 60)
                return response
            else:
                response.delete_cookie('login', path='/login/')
                return response

        else:
            response.delete_cookie('login', path='/login/')
            return HttpResponse('<script>alert("条件不全或有误,请检查后重输!");location.href="/login/";</script>')





def index_view(request):
    return render(request, 'index.html')