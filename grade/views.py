# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from login.models import *

#成绩录入
def grade_register_view(request):
    courses = Course.objects.all()
    if request.method == 'GET':
        return render(request,'grade_register.html',{'course':courses})
    else:
        try:
            if request.POST.get('submit', '') == '搜索':
                try:
                    id = request.POST.get('stu_id', '')
                    id = int(id)
                    stu = Stu.objects.get(stu_id=id)
                    return render(request, 'grade_register.html', {'stu': stu,'course':courses,})
                except:
                    return HttpResponse('<script>alert("无搜索条件，请重试");location.href="/grade/grade_register/";</script>')

            # 学生表  班级表  学生课程表  三表之间的班级表相互关联
            test_category = request.POST.get('test_category','')
            # 关联学生表和班级表
            stu_name = request.POST.get('stu_name','')
            stu_id = request.POST.get('stu_id','')
            stu_id = int(stu_id)
            clazz = request.POST.get('clazz','')
            # 通过班级名称的相等的方式获取信息     get获取必须要在表中有数据且页面输入与之相匹配
            clz = Clazz.objects.get(cls_name=clazz)
            stu = Stu.objects.get(stu_id=stu_id,stu_name=stu_name,clazz=clz,)
            if stu:
                for co in courses:
                    co1 = request.POST.get(co.cour_name)
                    StuScore.objects.create(stu=stu,clazz=clz,course=co,test_score=co1,test_category=test_category,)
                return HttpResponse('<script>alert("录入成功");location.href="/grade/grade_register/";</script>')

            else:
                return render(request, 'grade_register.html', {'course': courses})
        except:
            return HttpResponse('<script>alert("格式有误!");location.href="/grade/grade_register/";</script>')


#成绩查询
def grade_query_view(request):
    if request.method == 'GET':
        return render(request, 'grade_query.html')
    else:
        try:
            test_category = request.POST.get('test_category','')
            if test_category == '1':
                stu_id = request.POST.get('condition','')
                codes = Stu.objects.get(stu_id=stu_id).stuscore_set.all()
                return render(request,'grade_query.html',{'codes':codes,'code':stu_id})
            else:
                stu_name = request.POST.get('condition','')
                codes = Stu.objects.get(stu_name=stu_name).stuscore_set.all()
                return render(request, 'grade_query.html', {'codes': codes, 'code': stu_name})
        except:
            return HttpResponse('<script>alert("搜索条件有误!");location.href="/grade/grade_query/";</script>')


#班级成绩统计
def grade_claz_view(request):
    clz = Clazz.objects.all()
    course = Course.objects.all()
    if request.method == 'GET':
        return render(request, 'grade_claz.html', {'clz': clz, 'course': course})
    else:
        try:
            clazz = int(request.POST.get('clazz', ''))
            test_category = request.POST.get('test_category', '')

            stus = Clazz.objects.get(c_id=clazz).stu_set.all()
            datas = {}
            for stu in stus:
                score = []
                data = StuScore.objects.filter(stu=stu,test_category=test_category)
                # print data
                it = 0
                for ds in data:
                    st = ds.stu.stu_name
                    a = ds.test_score
                    it += a
                    score.append(a)
                score.append(it)
                datas[st] = score#用字典记住-键：学生，值：各科分数
            return render(request, 'grade_claz.html', {'clz': clz, 'datas': datas, 'course': course, 'test_category': test_category})
        except:
            return HttpResponse('<script>alert("此类成绩不存在!");location.href="/grade/grade_claz/";</script>')


#年级成绩统计
def grade_clazz_view(request):
    grades = Grade.objects.all()
    cour= Course.objects.all()
    if request.method == 'GET':
        return render(request, 'grade_clazz.html',{'grades':grades,'cour':cour})
    else:
        try:
            gra_id = request.POST.get('gra_id','')
            test_category = request.POST.get('test_category','')
            clazz = Grade.objects.get(gra_id=gra_id).clazz_set.all()
            datas = {}
            for clss in clazz:
                da = []
                clz = clss.cls_name
                # 学生人数
                counts = StuScore.objects.filter(clazz=clss,test_category=test_category).count()
                cr = cour.count()
                count = counts/cr
                da.append(count)
                #考试类型
                da.append(test_category)
                # 科目平均分
                su = 0
                for co in cour:
                    cas = StuScore.objects.filter(clazz=clss,test_category=test_category,course=co)
                    print cas
                    lenth = cas.count()#数值和学生数一致
                    a = 0
                    for c in cas:
                        c1 = c.test_score
                        a += c1
                    avg = a/lenth
                    da.append(avg)
                    su += a
                da.append(su)
                datas[clz] = da
                print datas
            return render(request, 'grade_clazz.html', {'grades': grades,'cour':cour,'datas':datas})
        except:
            return HttpResponse('<script>alert("此类成绩不存在!");location.href="/grade/grade_clazz/";</script>')
