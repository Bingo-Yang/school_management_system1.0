# coding=utf-8
from __future__ import unicode_literals

from django.db import models
# Create your models here.

#图书表
class Book(models.Model):
    #_id主键
    book_id = models.IntegerField(primary_key=True)
    # 图书名
    book_name = models.CharField(max_length=20, blank=True, null=True)
    #图书作者
    book_author = models.CharField(max_length=20, blank=True, null=True)
    # 图书出版社
    book_pub = models.CharField(max_length=20, blank=True, null=True)
    # 操作员
    book_operator = models.CharField(max_length=20, blank=True, null=True)
    # 图书入库数量
    book_put_num = models.CharField(max_length=20,blank=True, null=True)
    # 入库日期
    book_put_date = models.DateField(auto_now_add=True)
    # 图书分类
    book_category = models.CharField(max_length=20, blank=True, null=True)
    # 图书出版数量
    book_pub_num = models.CharField(max_length=20,blank=True, null=True)
    # 图书价格
    book_price = models.DecimalField(max_digits=6,decimal_places=2)
    # 图书出版日期
    book_pub_date = models.DateField(auto_now_add=True)
    # 图书简介
    book_intro = models.TextField()


    def __unicode__(self):
        return u'图书:%s' % self.book_name

    class Meta:
        db_table = 't_book'

# 课程表
class Course(models.Model):
    cour_id = models.IntegerField(primary_key=True, unique=True)
    # 课程名称
    cour_name = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __unicode__(self):
        return r'course:%s' % self.cour_name

    class Meta:
        db_table = 't_course'

# 年级表
class Grade(models.Model):
    gra_id = models.IntegerField(primary_key=True, unique=True)
    gra_name = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __unicode__(self):
        return u'年级:%s' % self.gra_name

    class Meta:
        db_table = 't_grade'

# 专业表
class Major(models.Model):
    maj_id = models.IntegerField(primary_key=True, unique=True)
    # 专业名称
    maj_name = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __unicode__(self):
        return u'专业:%s' % self.maj_name

    class Meta:
        db_table = 't_major'

# 班级表
class Clazz(models.Model):
    c_id = models.IntegerField(primary_key=True)
    # 班级名称
    cls_name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    # 外键关联年级/专业表
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'班级:%s' % self.cls_name

    class Meta:
        db_table = 't_class'
# 政治面貌表
# class Political(models.Model):
#     p_id = models.AutoField()
#     stu_political = models.CharField(max_length=10, blank=True, null=True,unique=True)
# 学生信息表
class Stu(models.Model):
    stu_id = models.IntegerField(primary_key=True, unique=True)
    # 外键关联班级表
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    # 性别
    stu_gender = models.CharField(max_length=2, blank=True, null=True)
    # 身份证号
    stu_id_num = models.CharField(max_length=20, blank=True, null=True)
    # 地址
    stu_addr = models.CharField(max_length=50, blank=True, null=True)
    # 政治面貌
    stu_political = models.CharField(max_length=10, blank=True, null=True)#改动
    # 健康状况
    stu_healthy = models.CharField(max_length=10, blank=True, null=True)#改动
    stu_name = models.CharField(max_length=15, blank=True, null=True)
    stu_age = models.IntegerField(blank=True, null=True)
    stu_birthday = models.DateField(blank=True, null=True)
    stu_phone = models.CharField(max_length=11, blank=True, null=True,unique=True)#位数有问题CharField
    # 民族
    stu_nation = models.CharField(max_length=3, blank=True, null=True)

    def __unicode__(self):
        return u'学生:%s' % self.stu_name

    class Meta:
        db_table = 't_stu_messenger'

#图书借阅表
class BookBorrow(models.Model):
    borrow_id = models.IntegerField(primary_key=True)
    #外键：图书表/学生表
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    stu = models.ForeignKey(Stu,on_delete=models.CASCADE)
    #借还书时间
    borrow_time = models.DateField(auto_now_add=True)
    return_time = models.DateField(auto_now_add=True)
    #操作员
    registrar = models.CharField(max_length=15, blank=True, null=True)

    def __unicode__(self):
        return u'图书:%s,借阅人:%s' % (self.book.book_name,self.stu.stu_name)

    class Meta:
        db_table = 't_book_borrow'

# 教师表
class Teacher(models.Model):
    tea_id = models.IntegerField(primary_key=True, unique=True)
    # 外键关联专业表
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    tea_name = models.CharField(max_length=20, blank=True, null=True)
    tea_gender = models.CharField(max_length=3, blank=True, null=True)
    # 政治面貌
    tea_political = models.CharField(max_length=20, blank=True, null=True)
    # 学历
    tea_edu = models.CharField(max_length=20, blank=True, null=True)
    # 身份证
    tea_id_num = models.CharField(max_length=20, blank=True, null=True)
    # 工作日期
    tea_work_date = models.DateField(blank=True, null=True)
    tea_age = models.IntegerField(blank=True, null=True)
    # 婚否
    tea_marry = models.CharField(max_length=10, blank=True, null=True)
    # 民族
    tea_natioin = models.CharField(max_length=10, blank=True, null=True)

    tea_birth = models.DateField(blank=True, null=True)
    tea_phone = models.CharField(max_length=11,blank=True, null=True)
    tea_intro = models.TextField()

    class Meta:
        db_table = 't_teacher'

# 班主任任职表
class HeadTeacher(models.Model):
    ht_id = models.AutoField(primary_key=True)
    #外键关联教师/班级表
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    clazz = models.OneToOneField(Clazz,on_delete=models.CASCADE)
    #入职日期
    ht_in_date = models.DateField(auto_now_add=True)
    #离职日期
    ht_out_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'班主任:%s班级:%s'%(self.teacher.tea_name,self.clazz.cls_name)

    class Meta:
        db_table = 't_head_teacher'



#学生入学登记表
class StuRegister(models.Model):
    sr_id = models.IntegerField(primary_key=True)#可以设自增
    #外键关联学生表/班级表
    stu = models.OneToOneField(Stu)
    clazz = models.ForeignKey(Clazz,on_delete=models.CASCADE)
    #学生专业
    stu_major = models.CharField(max_length=12, blank=True, null=True)
    #推荐人
    stu_recommender = models.CharField(max_length=10, blank=True, null=True)
    #入学时间
    stu_enrollment = models.DateField(blank=True, null=True)
    #入学成绩
    stu_score = models.IntegerField(blank=True, null=True)#改动

    def __unicode__(self):
        return u'学生登记:%s'%self.stu.stu_name

    class Meta:
        db_table = 't_stu_register'

#学生课程成绩表
class StuScore(models.Model):
    sco_id = models.AutoField(primary_key=True)
    #外键关联学生/班级/课程表
    stu = models.ForeignKey(Stu,on_delete=models.CASCADE)
    clazz = models.ForeignKey(Clazz,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    #负责老师
    test_teacher = models.CharField(max_length=20, blank=True, null=True)
    #考试时间
    test_date = models.DateField(blank=True, null=True)
    #考试类别
    test_category = models.CharField(max_length=20, blank=True, null=True)
    #考试分数
    test_score = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    def __unicode__(self):
        return u'学生:%s,成绩:%s'%(self.stu.stu_name,self.course.cour_name)
    class Meta:
        db_table = 't_stu_score'


# 教师任课表
class TeachingStaff(models.Model):
    ts_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    #任课时间
    tea_in_date = models.DateField(blank=True, null=True)
    #结课时间
    tea_out_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return u'教师:%s,课程:%s'%(self.teacher.tea_name,self.course.cour_name)

    class Meta:
        db_table = 't_teaching_staff'

#用户登录表
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=15, blank=True, null=True,unique=True)
    user_password = models.CharField(max_length=20, blank=True, null=True)
    #昵称
    user_nickname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 't_user'
