# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from login.models import Major, Grade, Clazz, Course


def maintain(request):
    if request.session.get('uname','') != 'uname':
        majors = Major.objects.all().order_by('maj_id')
        if request.method == 'GET':

            return render(request,'maintain.html',{'majors':majors})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request,'power.html',{'con':con})


def change(request,code,name,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request, 'change.html', {'code': code, 'name': name})
        else:
            code1 = int(request.POST.get('code', ''))
            name1 = request.POST.get('name', '')
            print code1, name1
            if code1 and name1:
                try:
                    Major.objects.filter(maj_id=code, maj_name=name).update(maj_id=code1, maj_name=name1)
                    return redirect('/maintenance/maintain/')
                except:
                    con = '专业代码/专业名称已存在。'
                    return render(request,'power.html',{'con': con})
            else:
                con = '输入不能为空。'
                return render(request, 'power.html', {'con': con})
    else:
        Major.objects.filter(maj_id=code, maj_name=name).delete()
        return redirect('/maintenance/maintain/')


def grade(request):
    if request.session.get('uname','') != 'uname':
        grades = Grade.objects.all().order_by('gra_id')
        if request.method == 'GET':
            return render(request,'grad.html',{'grades':grades})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request,'power.html',{'con':con})


def change1(request,code,name,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request, 'chang1.html', {'code': code, 'name': name})
        else:
            code1 = int(request.POST.get('code', ''))
            name1 = request.POST.get('name', '')
            if code1 and name1:
                try:
                    Grade.objects.filter(gra_id=code, gra_name=name).update(gra_id=code1, gra_name=name1)
                    return redirect('/maintenance/grade/')
                except:
                    con = '年级代码/年级名称已存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request, 'power.html', {'con': con})
    else:
        Grade.objects.filter(gra_id=code, gra_name=name).delete()
        return redirect('/maintenance/grade/')


def clazz(request):
    if request.session.get('uname','') != 'uname':
        cls = Clazz.objects.all().order_by('c_id')
        if request.method == 'GET':
            return render(request,'cl.html',{'cls':cls})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request,'power.html',{'con':con})


def change2(request,code,name,gr,mj,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request, 'change2.html', {'code': code, 'name': name, 'grade': gr, 'major': mj})
        else:
            code1 = int(request.POST.get('code', ''))
            name1 = request.POST.get('name', '')
            gr1 = request.POST.get('grade', '')
            mj1 = request.POST.get('major', '')
            if code1 and name1 and gr and mj:
                try:
                    gr2 = Grade.objects.get(gra_name=gr1)
                    mj2 = Major.objects.get(maj_name=mj1)
                    Clazz.objects.filter(c_id=code, cls_name=name).update(c_id=code1, cls_name=name1, grade=gr2,major=mj2)
                    return redirect('/maintenance/clazz/')
                except:
                    con = '班级代码/班级名称已存在/专业名称不存在/年级名称不存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request, 'power.html', {'con': con})
    else:
        Clazz.objects.filter(c_id=code, cls_name=name).delete()
        return redirect('/maintenance/clazz/')


def course(request):
    if request.session.get('uname', '') != 'uname':
        courses = Course.objects.all().order_by('cour_id')
        if request.method == 'GET':
            return render(request, 'course.html', {'courses': courses})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request, 'power.html', {'con': con})


def change3(request,code,name,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request, 'change3.html', {'code': code, 'name': name})
        else:
            code1 = int(request.POST.get('code', ''))
            name1 = request.POST.get('name', '')
            if code1 and name1:
                try:
                    Course.objects.filter(cour_id=code, cour_name=name).update(cour_id=code1, cour_name=name1)
                    return redirect('/maintenance/course/')
                except:
                    con = '学科代码/学科名称已存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request, 'power.html', {'con': con})
    else:
        Major.objects.filter(maj_id=code, maj_name=name).delete()
        return redirect('/maintenance/course/')