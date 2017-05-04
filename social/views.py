from django.shortcuts import render
from django.template import context
from django.views.generic import DetailView
from django.views.generic import ListView

import blog
from blog.models import Blog
from comments.models import CommentsBlog, CommentsNews
from news.models import *
from .models import *


# Create your views here.

def index(request):
    social = SocialLinks.objects.first()
    _news = News.objects.all().order_by('-date')[:4]
    blog = Blog.objects.all().order_by('-date')[:4]

    params = {
        'social': social,
        'news': _news,
        'blog': blog,
    }

    return render(request, 'index.html', params)


# def get_news(request, id):
#     news = News.objects.filter(id=id).first()
#
#     params = {
#         'news': news,
#     }
#
#     return render(request, 'detail.html', params)
#
#
# def get_blog(request, id):
#     blog = Blog.objects.filter(id=id).first()
#     #
#     # params = {
#     #     'blog': blog,
#     # }
#     #
#     # return render(request, 'detail.html', params)


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        return context


class NewsListView(BlogListView):
    model = News


class GetBlogView(DetailView):
    # context_object_name = 'blog'
    # template_name = 'blog/blog_detail.html'
    # # def get_template_names(self):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(GetBlogView, self).get_context_data(**kwargs)
        context['comments'] = CommentsBlog.objects.last()
        return context


class GetNewsView(DetailView):
    # def get_context_data(self, **kwargs):
    #     context = super(GetNewsView, self).get_context_data(**kwargs)
    #     context['news'] = News.objects.filter(id=id)
    #     return context
    model = News

    def get_context_data(self, **kwargs):
        context = super(GetNewsView, self).get_context_data(**kwargs)
        context['comments'] = CommentsNews.objects.last()
        return context
