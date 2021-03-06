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
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name="archives"),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

]