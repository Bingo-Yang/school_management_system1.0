#coding=utf-8
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from login.models import Clazz, Stu, StuRegister, Major, Teacher


# 学生信息注册
def stu_info_view(request):
    if request.method == 'GET':
        # 根据班级名称查询班级
        clazzs = Clazz.objects.all()
        stus = Stu.objects.all()
        return render(request,'stu_info.html',{'clazzs':clazzs,'stus':stus,})
    else:
        try:
        #获取录入数据
            clazz = request.POST.get('clazz', '')
            cls = Clazz.objects.get(cls_name=clazz)#获取班级表信息
            political = request.POST.get('political', '')
            id = request.POST.get('id', '')
            id = int(id)#字符串转数据库int型
            name = request.POST.get('name', '')
            gender = request.POST.get('gender', '')
            healthy = request.POST.get('healthy', '')
            id_num = request.POST.get('id_num', '')
            birth = request.POST.get('birth', '')
            nation = request.POST.get('nation', '')
            age = request.POST.get('age', '')
            age = int(age)
            addr = request.POST.get('addr', '')
            phone = request.POST.get('phone', '')
            # 存入学生数据库
            Stu.objects.create(stu_id=id,clazz=cls,stu_gender=gender,
                               stu_id_num=id_num,stu_addr=addr,stu_political=political,
                               stu_healthy=healthy,stu_name=name,stu_phone=phone,
                               stu_age=age,stu_birthday=birth,stu_nation=nation)
            return HttpResponse('<script>alert("注册成功!");location.href="/archive/student/";</script>')
        except:
            return HttpResponse('<script>alert("条件不全或有误,请检查后重输!");location.href="/archive/student/";</script>')

# 学生入校登记
def stu_school_register(request):
    if request.method == 'GET':
        return render(request, 'stu_school_register.html')
    else:
        if request.POST.get('submit', '') == '确定':
            try:
                id = request.POST.get('id','')
                id = int(id)
                stu = Stu.objects.get(stu_id=id)
                return render(request,'stu_school_register2.html',{'stu':stu})
            except:
                return HttpResponse('<script>alert("无查询条件，请重试");location.href="/archive/register/";</script>')

        #点提交获取数据存入数据库
        elif request.POST.get('submit', '') == '提交':
            try:
                name = request.POST.get('name','')
                stu = Stu.objects.get(stu_name=name)
                clazz = request.POST.get('clazz', '')
                cls = Clazz.objects.get(cls_name=clazz)
                major = request.POST.get('major', '')
                enrollment = request.POST.get('enrollment','')
                recommender = request.POST.get('recommender','')
                score = request.POST.get('score','')
                StuRegister.objects.create(stu=stu,clazz=cls,stu_major=major,stu_recommender=recommender
                                           ,stu_enrollment=enrollment,stu_score=score,sr_id=stu.stu_id)
                return HttpResponse('<script>alert("注册成功!");location.href="/archive/register/";</script>')
            except:
                return HttpResponse('<script>alert("条件不全或有误,请检查后重输!");location.href="/archive/register/";</script>')
        #点重置返回初始页
        elif request.POST.get('submit','') == '重置':#类型写submit防止冲突
            return render(request, 'stu_school_register.html')


# 学生信息系统维护
def stu_info_maintenance(request,num):
    if request.method == 'GET':
        #有参数获取session
        if num:
            # global num1
            # num1 = num
            #获取session
            stu_str = request.session.get('stus')
            #删除session
            # del request.session['stus']
            #将字符串切成列表
            stu_list = stu_str.split(',')
            #遍历列表查出学生存进stus列表，传进网页
            stus = []
            #将num转为int型,长编号用long
            num = int(num)
            for stu_id in stu_list:
                stu = Stu.objects.get(stu_id=stu_id)
                stus.append(stu)
            return render(request,'stu_info_maintenance.html',{'num':num,'stus':stus})

        else:
            return render(request, 'stu_info_maintenance.html')
    #没有参数返回普通页面
    else:
        if request.POST.get('submit','') == '查询':
            try:
                select = request.POST.get('select','')
                query = request.POST.get('query','')
                if select == '学生编号':
                    query = int(query)
                    stus = Stu.objects.filter(stu_id=query)
                    #创建学生列表
                    stu_list = []
                    #循环遍历将学生id加入列表
                    for stu in stus:
                        stu_list.append(str(stu.stu_id))
                    #把列表合成字符串
                    stu_str = ','.join(stu_list)
                    #把字符串存进session
                    request.session['stus'] = stu_str
                    return render(request, 'stu_info_maintenance.html', {'stus': stus})
                elif select == '学生姓名':
                    stus = Stu.objects.filter(stu_name=query)
                    # 创建学生列表
                    stu_list = []
                    # 循环遍历将学生id加入列表
                    for stu in stus:
                        stu_list.append(str(stu.stu_id))
                    # 把列表合成字符串
                    stu_str = ','.join(stu_list)
                    # 把字符串存进session
                    request.session['stus'] = stu_str
                    return render(request, 'stu_info_maintenance.html', {'stus': stus})
                elif select == '身份证号':
                    stus = Stu.objects.filter(stu_id_num=query)
                    # 创建学生列表
                    stu_list = []
                    # 循环遍历将学生id加入列表
                    for stu in stus:
                        stu_list.append(str(stu.stu_id))
                    # 把列表合成字符串
                    stu_str = ','.join(stu_list)
                    # 把字符串存进session
                    request.session['stus'] = stu_str
                    return render(request, 'stu_info_maintenance.html', {'stus': stus})
                elif select == '班级名称':
                    stus = Clazz.objects.get(cls_name=query).stu_set.all()
                    # 创建学生列表
                    stu_list = []
                    # 循环遍历将学生id加入列表
                    for stu in stus:
                        stu_list.append(str(stu.stu_id))
                    # 把列表合成字符串
                    stu_str = ','.join(stu_list)
                    # 把字符串存进session
                    request.session['stus'] = stu_str
                    return render(request, 'stu_info_maintenance.html', {'stus': stus})
            except:
                return HttpResponse('<script>alert("无查询条件，请重试");location.href="/archive/maintenance/";</script>')
        elif request.POST.get('submit', '') == '提交':
            try:
                name = request.POST.get('name','')
                id_num = request.POST.get('id_num','')
                #获取生日字符串转为date格式
                birth = request.POST.get('birth','')
                birth = datetime.strptime(birth,'%Y-%m-%d')
                addr = request.POST.get('addr','')
                id = request.POST.get('id','')
                id = int(id)
                Stu.objects.filter(stu_id=id).update(stu_name=name,stu_id_num=id_num,stu_birthday=birth,stu_addr=addr)
                return HttpResponse('<script>alert("学生信息修改成功!");location.href="/archive/maintenance/";</script>')
            except:
                return HttpResponse('<script>alert("学生信息修改失败!");location.href="/archive/maintenance/";</script>')


#学生登记查询
def stu_register_query(request):
    if request.method == 'GET':
        return render(request,'stu_register_query.html')
    else:
        try:
        # 获取网页信息
            field = request.POST.get('field','')
            operator = request.POST.get('operator','')
            message = request.POST.get('message','')
            #根据学号查询
            if field == '学生编号':
                message = int(message)
                if operator == '大于':
                    stus = Stu.objects.filter(stu_id__gt=message)
                    return render(request,'stu_register_query.html',{'stus':stus})
                elif operator == '等于':
                    stus = Stu.objects.filter(stu_id=message)
                    return render(request,'stu_register_query.html',{'stus':stus})
                elif operator == '小于':
                    stus = Stu.objects.filter(stu_id__lte=message)
                    return render(request,'stu_register_query.html',{'stus':stus})
            elif field == '入学日期':
                message = datetime.strptime(message,'%Y-%m-%d')
                if operator == '大于':
                    #把所有日期大于message的学生对象存入列表
                    stus = []
                    for stu in StuRegister.objects.filter(stu_enrollment__gt=message):
                        stus.append(stu.stu)
                    return render(request,'stu_register_query.html',{'stus':stus})
                elif operator == '等于':
                    stus = []
                    for stu in StuRegister.objects.filter(stu_enrollment=message):
                        stus.append(stu.stu)
                    return render(request,'stu_register_query.html',{'stus':stus})
                elif operator == '小于':
                    stus = []
                    for stu in StuRegister.objects.filter(stu_enrollment__lte=message):
                        stus.append(stu.stu)
                    return render(request,'stu_register_query.html',{'stus':stus})
            elif field == '录取分数':
                if operator == '大于':
                    stus = []
                    for stu in StuRegister.objects.filter(stu_score__gt=message):
                        stus.append(stu.stu)
                    return render(request,'stu_register_query.html',{'stus':stus})
                elif operator == '等于':
                    stus = []
                    for stu in StuRegister.objects.filter(stu_score=message):
                        stus.append(stu.stu)
                    return render(request,'stu_register_query.html',{'stus':stus})
                elif operator == '小于':
                    stus = []
                    for stu in StuRegister.objects.filter(stu_score__lte=message):
                        stus.append(stu.stu)
                    return render(request,'stu_register_query.html',{'stus':stus})
        except:
            return HttpResponse('<script>alert("查询条件有误");location.href="/archive/query/";</script>')

    #教师基本信息登记及后面表的查询

#老师基本信息
def tea_info_view(request,num):
    if request.method == 'GET':
        # 根据班级名称查询班级
        global num1
        num1 = num
        if num1:
            majors = Major.objects.all()
            teacher = Teacher.objects.get(tea_id=num1)
            return render(request, 'tea_update.html', {'teacher': teacher,'majors':majors,})
        else:
            majors = Major.objects.all()
            return render(request, 'teacher_info.html', {'majors': majors, })
    elif request.POST.get('submit', '') == '提交':
        try:
            # 获取录入数据
            name = request.POST.get('name', '')
            id = request.POST.get('id', '')
            id = int(id)
            marry = request.POST.get('marry', '')
            gender = request.POST.get('gender', '')
            age = request.POST.get('age', '')
            id_num = request.POST.get('id_num', '')
            birth = request.POST.get('birth', '')
            political = request.POST.get('political', '')
            nation = request.POST.get('nation', '')
            edu = request.POST.get('edu', '')
            work_date = request.POST.get('work_date', '')
            phone = request.POST.get('phone', '')
            major = request.POST.get('major', '')
            major = Major.objects.get(maj_name=major)#获取专业表表信息
            intro = request.POST.get('intro', '')
            Teacher.objects.create(tea_id=id, major=major, tea_name=name, tea_gender=gender, tea_political=political, tea_marry=marry,
                                   tea_edu=edu, tea_id_num=id_num, tea_work_date=work_date, tea_age=age,tea_natioin=nation,
                                   tea_birth=birth,tea_phone=phone,tea_intro=intro)
            return HttpResponse('<script>alert("教师信息注册成功!");location.href="/archive/teacher/";</script>')
        except:
            return HttpResponse('<script>alert("教师信息不全或有误,请重输!");location.href="/archive/teacher/";</script>')
    elif request.POST.get('submit', '') == '修改':
        try:
            # 修改录入数据
            name = request.POST.get('name', '')
            id = request.POST.get('id', '')
            id = int(id)
            marry = request.POST.get('marry', '')
            gender = request.POST.get('gender', '')
            age = request.POST.get('age', '')
            id_num = request.POST.get('id_num', '')
            birth = request.POST.get('birth', '')
            political = request.POST.get('political', '')
            nation = request.POST.get('nation', '')
            edu = request.POST.get('edu', '')
            work_date = request.POST.get('work_date', '')
            phone = request.POST.get('phone', '')
            major = request.POST.get('major', '')
            major = Major.objects.get(maj_name=major)#获取专业表表信息
            intro = request.POST.get('intro', '')
            Teacher.objects.filter(tea_id=num1).update(tea_id=id, major=major, tea_name=name, tea_gender=gender, tea_political=political, tea_marry=marry,
                                   tea_edu=edu, tea_id_num=id_num, tea_work_date=work_date, tea_age=age,tea_natioin=nation,
                                   tea_birth=birth,tea_phone=phone,tea_intro=intro)
            return HttpResponse('<script>alert("教师信息修改成功!");location.href="/archive/teaMaintenance/";</script>')
        except:
            return HttpResponse('<script>alert("教师信息修改有误,请重输!");location.href="/archive/teaMaintenance/";</script>')
    elif request.POST.get('submit', '') == '重置':
        return render(request, 'tea_reset.html')

#教师信息维护
def tea_info_maintenance(request):
    if request.method == 'GET':
        return render(request, 'tea_info_maintenance.html')
    else:
        try:
            if request.POST.get('submit','') == '查询':
                select = request.POST.get('select', '')
                query = request.POST.get('query', '')
                if select == '教师编号':
                    query = int(query)
                    teachers = Teacher.objects.filter(tea_id=query)
                    return render(request,'tea_info_maintenance.html',{'teachers':teachers})
                elif select == '教师姓名':
                    teachers = Teacher.objects.filter(tea_name=query)
                    return render(request,'tea_info_maintenance.html',{'teachers':teachers})
                elif select == '专业名称':
                    teachers = Major.objects.get(maj_name=query).teacher_set.all()
                    return render(request,'tea_info_maintenance.html',{'teachers':teachers})
        except:
            return HttpResponse('<script>alert("查询条件有误,请重试");location.href="/archive/teaMaintenance/";</script>')