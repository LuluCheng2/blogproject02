#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2018/11/20
# __author__ = "Lulu Cheng"
'''
# comments/forms.py
# 评论表单
'''

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 表单对应的数据库模型是 Comment 类
        fields = ['name', 'email', 'url', 'text']  # 表单需要显示的字段

