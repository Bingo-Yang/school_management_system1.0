# coding= utf-8
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from login.models import *

# Create your views here.
#主页面
def teacher_view(request):
    return render(request,'base.html')

#教职工展示页面
def showtea_view(request):
    if request.method=='GET':
        # 导入课程表
        cose=Course.objects.all()
        #导入老师表
        teaxinxis=Teacher.objects.all()
        return render(request,'teacher.html',{'cose':cose,'teaxinxis':teaxinxis})
    else:
        try:
            #教师编号
            te_id=request.POST.get('t_id','')

            tea_id=Teacher.objects.get(tea_id=te_id)

            #任职科目
            tea_course=request.POST.get('tea_course','')
            #任职日期
            tea_date=request.POST.get('tea_date','')

            # 教师任课表
            TeachingStaff.objects.create(tea_in_date=tea_date,teacher=tea_id,course=Course.objects.get(cour_id=tea_course))

            return HttpResponse('<script>alert("关联教师任职表成功！点击确定返回页面");location.href="/teach/show/";</script>')
        except:
            return HttpResponse('<script>alert("搞错了，滚回去重弄！");location.href="/teach/show/";</script>')


#创建班主任外键
def guide_view(request):
    if request.method=='GET':
        #班级表
        cls = Clazz.objects.all()
        # 导入老师表
        teaxinxis = Teacher.objects.all()
        return render(request,'guide.html',{'cls':cls,'teaxinxis':teaxinxis})
    else:
        try:
            #请输入教师编号
            guide_id = request.POST.get('guide_id', '')
            #班级名称
            clazz = request.POST.get('clazz','')
            #任职日期
            service_date = request.POST.get('service_date','')
            # 离职日期
            lizhi_date = request.POST.get('lizhi_date','')
            # 班主任任职表
            HeadTeacher.objects.create(ht_in_date=service_date,ht_out_date=lizhi_date,clazz = Clazz.objects.get(cls_name=clazz),teacher=Teacher.objects.get(tea_id=guide_id))
            return HttpResponse('<script>alert("关联班主任任职表成功！点击确定返回页面！");location.href="/teach/guide/";</script>')
        except:
            return HttpResponse('<script>alert("班主任任职失败，请确定该教师是否已是班主任！");location.href="/teach/guide/";</script>')




#展示任课教师信息
def coursetea_view(request):
    if request.method=='GET':
        ts_id = request.GET.get('ts_id')

        TeachingStaff.objects.filter(ts_id=ts_id).delete()
        return render(request,'show_coursetea.html')
    else:
        try:
            #查询
            query = request.POST.get('query','')
            #任职科目
            course = request.POST.get('course','')

            ts_id = request.POST.get('ts_id')


            if query=='任课科目编号':
                ct_course = TeachingStaff.objects.filter(course=course)
                return render(request, 'show_coursetea.html', {'ct_course':ct_course})

            if query=='教师编号':
                teacher = int(course)
                tsc=[]
                to = TeachingStaff.objects.filter(teacher=Teacher.objects.get(tea_id=teacher))
                for t in to:
                    tsc.append(t)

                return render(request, 'show2_coursetea.html',{'tsc':tsc})

        except:
            return HttpResponse('<script>alert("没找到，滚回去重找！");location.href="/teach/coursetea/";</script>')

#展示班主任班级
def showguide_view(request):
    if request.method=='GET':
        #班主任
        ht_id = request.GET.get('ht_id','')
        if ht_id:
            HeadTeacher.objects.filter(ht_id = ht_id).delete()
        return render(request,'show_guide.html')
    else:
        try:
            # 查询
            query = request.POST.get('query')
            #班级
            clazz = request.POST.get('clazz','')

            if query =='班级编号':

                g_clazz = HeadTeacher.objects.filter(clazz=Clazz.objects.get(c_id=clazz))

                return render(request,'show_guide.html',{'g_clazz':g_clazz})
            if query == '年级编号':

                grade = int(clazz)

                grade = int(grade)

                clazz = Grade.objects.get(gra_id=grade).clazz_set.all()
                tal = []
                for cl in clazz:

                    clz1 = HeadTeacher.objects.get(clazz=cl)

                    clz2 = Teacher.objects.get(tea_name=clz1.teacher.tea_name)

                    tal.append(clz2)
                cls=Clazz.objects.all()

                return render(request, 'show2_guide.html', {'tal': tal,'cls':cls})
        except:
            return HttpResponse('<script>alert("没找到，滚回去重找！");location.href="/teach/showguide/";</script>')

#展示班主任信息
def showguide2_view(request):
    if request.method=="GET":

        return render(request,'show_guide2.html')

    else:
        try:
            guide_id = request.POST.get('ht_id','')

            htr = HeadTeacher.objects.filter(clazz=Clazz.objects.get(c_id=guide_id))

            clz1 = Clazz.objects.all()

            hd = HeadTeacher.objects.filter(teacher=guide_id)

            return render(request,'show_guide2.html',{'htr':htr,'clz1':clz1,'hd':hd})
        except:
            return HttpResponse('<script>alert("没找到，滚回去重找！");location.href="/teach/showguide2/";</script>')




#查询任课教师信息
def querycoursetea_view(request):
    if request.method=='GET':
        return render(request,'query_coursetea.html')
    else:
        try:
            ts_id = request.POST.get('ts_id')
            tcs= TeachingStaff.objects.filter(teacher=ts_id)
            ct_all = Teacher.objects.all()
            return render(request,'query_coursetea.html',{'tcs':tcs,'ct_all':ct_all})
        except:
            return HttpResponse('<script>alert("没找到，滚回去重找！");location.href="/teach/querytea/";</script>')









