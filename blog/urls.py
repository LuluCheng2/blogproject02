#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2018/11/19
# __author__ = "Lulu Cheng"
'''
blog/urls.py
'''

from django.conf.urls import url
from . import views

# 视图函数命名空间
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name="archives"),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),

]