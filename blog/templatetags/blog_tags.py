#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2018/11/20
# __author__ = "Lulu Cheng"
'''
自定义的模板标签
'''
from django import template
from django.db.models.aggregates import Count
from ..models import Post, Category, Tag

register = template.Library()

# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

# 归类模板标签，按 创建时间 降序排序
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

# 分类模板标签
@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 标签模板标签
@register.simple_tag
def get_tags():
    # Count 计算标签下的文章数，其接受的参数为需要计数的模型的名称
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)



