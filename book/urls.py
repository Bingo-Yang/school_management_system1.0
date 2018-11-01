#coding=utf-8
from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^book_register/',views.book_register_view),
    url(r'^book_maintain/?(\d+)',views.book_maintain_view),
    url(r'^book_Borrow/',views.book_Borrow_view),
    url(r'^book_return/',views.book_return_view),
    url(r'^book_show/',views.book_show_view),
]