# blog/views.py
# coding:utf-8

import markdown
from django.shortcuts import render, get_object_or_404

from comments.forms import CommentForm
from .models import Post, Category

# 主页：文章列表页
def index(request):
    # all() 方法获取全部文章，order_by() 按created_time排序，- 表示逆序排序
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',  # 拓展功能
                                     'markdown.extensions.codehilite',  # 语法高亮功能
                                     'markdown.extensions.toc',  # 自动生成目录
                                  ])
    # 顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all().order_by('-created_time')

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据
    context = {'post': post,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'blog/detail.html', context=context)

# 文章按日期归档
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 文章分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})
