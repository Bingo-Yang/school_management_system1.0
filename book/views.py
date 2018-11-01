# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from login.models import Book, BookBorrow, Stu


#图书登记
def book_register_view(request):
    if request.method == 'GET':
        return render(request,'book_register.html')
    else:
        try:
            book_id = request.POST.get('book_id', '')
            book_id = int(book_id)
            book_author = request.POST.get('book_author', '')
            book_pub = request.POST.get('book_pub', '')
            book_operator = request.POST.get('book_operator', '')
            book_put_num = request.POST.get('book_put_num', '')
            book_put_date = request.POST.get('book_putdate', '')
            book_name = request.POST.get('book_name', '')
            book_category = request.POST.get('book_category', '')
            book_price = request.POST.get('book_price', '')
            book_pub_date = request.POST.get('book_pub_date ', '')
            book_intro = request.POST.get('book_intro ', '')
            Book.objects.create(book_author=book_author, book_pub=book_pub,
                                book_operator=book_operator, book_put_num=book_put_num,
                                book_put_date=book_put_date, book_name=book_name,
                                book_category=book_category, book_price=book_price,
                                book_pub_date=book_pub_date, book_intro=book_intro,
                                book_id=book_id
                                )
            return HttpResponse('<script>alert("注册成功!");location.href="/book/book_register/";</script>')
        except:
            return HttpResponse('<script>alert("条件不全或有误,请检查后重输!");location.href="/book/book_register/";</script>')

# 图书信息展示
def book_show_view(request):
    if request.method == 'GET':
        book = Book.objects.all().order_by('-book_operator')
        return render(request, 'book_show.html', {'book': book})
    else:
        try:
            if request.POST.get('choice') == 'book_id':
                # 搜索值书号
                content = request.POST.get('content', '')
                if content:
                    book = Book.objects.filter(book_id=content).all()
                    return render(request, 'book_show.html', {'book': book})
                return HttpResponse('<script>alert("无此书号!");location.href="/book/book_show/";</script>')
            elif request.POST.get('choice') == 'book_name':
                # 搜索值书名
                content = request.POST.get('content', '')
                # 搜索字段包含输入内容
                if content:
                    book = Book.objects.filter(book_name__contains=content).all()
                    return render(request, 'book_show.html', {'book': book})
                return HttpResponse('<script>alert("操作失败!");location.href="/book/book_show/";</script>')
            elif request.POST.get('choice') == 'book_author':
                # 搜索值作者
                content = request.POST.get('content', '')
                if content:
                    book = Book.objects.filter(book_author=content).all()
                    return render(request, 'book_show.html', {'book': book})
                return HttpResponse('<script>alert("无此作者!");location.href="/book/book_show/";</script>')
            elif request.POST.get('choice') == 'book_category':
                # 搜索值类型
                content = request.POST.get('content', '')
                if content:
                    book = Book.objects.filter(book_category__contains=content).all()
                    return render(request, 'book_show.html', {'book': book})
                return HttpResponse('<script>alert("操作失败!");location.href="/book/book_show/";</script>')
            elif request.POST.get('choice') == 'book_all':
                book = Book.objects.all().order_by('-book_operator')
                return render(request, 'book_show.html', {'book': book})
        except:
            return HttpResponse('<script>alert("搜索条件有误，请重试!");location.href="/book/book_show/";</script>')

#图书信息修改维护
def book_maintain_view(request,num):
    if request.method == 'GET':
        book = Book.objects.filter(book_id=num)
        return render(request, 'book_maintain.html', {'book': book})
    else:
        try:
            book_category=request.POST.get('book_category','')
            book_id=request.POST.get('book_id', '')
            book_name=request.POST.get('book_name', '')
            book_author=request.POST.get('book_author', '')
            book_pub=request.POST.get('book_pub', '')
            book_price=request.POST.get('book_price', '')
            book_operator=request.POST.get('book_operator', '')
            book_put_num=request.POST.get('book_put_num', '')
            Setbook(num,book_category,book_id,book_name,book_author,book_pub,book_price,book_operator,book_put_num)
            return redirect('/book/book_show/')
        except:
            return HttpResponse('<script>alert("修改条件有误!请重试");location.href="/book/book_show/";</script>')

def Setbook(num,book_category,book_id,book_name,book_author,book_pub,book_price,book_operator,book_put_num):
    Book.objects.filter(book_id=num).update(book_category=book_category, book_id=book_id,book_name=book_name, book_author=book_author,book_pub=book_pub,
                                            book_price=book_price, book_operator=book_operator, book_put_num=book_put_num)


#图书借阅归还
def book_Borrow_view(request):
    if request.method == 'GET':
        return render(request, 'book_Borrow.html')
    else:
        try:
            # 获取书的书号
            book_id = request.POST.get('book_id', '')
            # 获取书的对象
            book = Book.objects.get(book_id=book_id)
            # 获取学生id
            stu_id = request.POST.get('stu_id', '')
            stu = Stu.objects.get(stu_id=stu_id)
            # 获取借阅开始时间
            borrow_time = request.POST.get('borrow_time', '')
            #获取借阅id
            borrow_id = request.POST.get('borrow_id', '')
            # 获取归还时间
            return_time = request.POST.get('return_time', '')
            # 获取登记负责人
            registrar = request.POST.get('registrar', '')
            borrow = BookBorrow.objects.create(book=book, stu=stu, borrow_time=borrow_time, return_time=return_time, registrar=registrar, borrow_id=borrow_id)
            if borrow:
                return HttpResponse('<script>alert("借阅成功!");location.href="/book/book_Borrow/";</script>')
        except:
            return HttpResponse('<script>alert("借阅登记失败!");location.href="/book/book_Borrow/";</script>')


# 图书借阅归还展示
def book_return_view(request):
    if request.method == 'GET':
        borrow = BookBorrow.objects.all().order_by('-borrow_time')
        return render(request, 'book_return.html', {'borrow': borrow})
    else:
        # 搜索书号
        if request.POST.get('choice') == 'book_id':
            content = request.POST.get('content', '')
            if content:
                borrow = BookBorrow.objects.filter(book_id=content).all()
                #print borrow
                if borrow:
                    return render(request, 'book_return.html', {'borrow': borrow})
            return HttpResponse('<script>alert("无此书号!");location.href="/book/book_return/";</script>')

        # 搜索书名
        elif request.POST.get('choice') == 'book_name':
            content = request.POST.get('content', '')
            if content:
                # 获取图书集合
                book_set = Book.objects.filter(book_name__contains=content).all()
                #print book_set
                borrow = []
                for bo in book_set:
                    book_id = bo.book_id
                    borrow_set = BookBorrow.objects.filter(book_id=book_id).all()
                    # print borrow_set
                    borrow.append(borrow_set)
                #print borrow
                return render(request, 'book_return1.html', {'borrow': borrow})
            return HttpResponse('<script>alert("图书名查询条件为空!");location.href="/book/book_return/";</script>')

        # 搜索学号
        elif request.POST.get('choice') == 'stu_id':

            content = request.POST.get('content', '')
            if content:
                borrow = BookBorrow.objects.filter(stu_id=content).all()
                if borrow:
                    return render(request, 'book_return.html', {'borrow': borrow})
            return HttpResponse('<script>alert("无此学号!");location.href="/book/book_return/";</script>')

        # 搜索图书种类
        elif request.POST.get('choice') == 'book_category':
            # 搜索值类型borrow
            content = request.POST.get('content', '')
            borrow = Book.objects.filter(book_category__contains=content).all()
            return render(request, 'book_return.html', {'borrow': borrow})
        elif request.POST.get('choice') == 'borrow_all':
            borrow = BookBorrow.objects.all().order_by('-borrow_time')
            return render(request, 'book_return.html', {'borrow': borrow})




