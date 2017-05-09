# coding=utf-8
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.models import Blog
from comments.forms import CommentBlogForm, CommentNewsForm
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


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['social'] = SocialLinks.objects.first()

        return context


# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blog/blog_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogDetailView, self).get_context_data(**kwargs)
#         context['comments'] = CommentsBlog.objects.all()
#         context['form'] = CommentBlogForm()
#         return context


def get_blog(request, id):
    blog = Blog.objects.get(id=id)
    comments = CommentsBlog.objects.filter(blog_id=blog)
    form = CommentBlogForm(request.POST)

    params = {
        'blog':blog,
        'comments':comments,
        'form':form,
    }

    return render(request, 'blog/blog_detail.html', params)

def comments_add(request):
    if request.is_ajax():
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            comment = CommentsBlog()
            comment.email = form.cleaned_data['email']
            comment.blog_id = form.cleaned_data['blog']
            comment.text = form.cleaned_data['text']
            comment.save()

            return JsonResponse(dict(success=True))

    return JsonResponse(dict(success=True, message='Request is not AJAX!'))

@csrf_exempt
def comments_all(request):
    comments = CommentsBlog.objects.filter(blog_id=request.POST.get('blog'))

    params = {
        'comments': comments
    }
    return render_to_response('partial/_comments.html', params)


class NewsListView(BlogListView):
    model = News


# class NewsDetailView(DetailView):
#     model = News
#
#     def get_context_data(self, **kwargs):
#         context = super(NewsDetailView, self).get_context_data(**kwargs)
#         context['comments'] = CommentsNews.objects.all()
#
#         return context


def add_news_comment(request, id):
    news = News.objects.get(id=id)
    comments = CommentsNews.objects.all()
    form = CommentNewsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news_id = news.id
            comment.save()

    params = {
        'form': form,
        'news': news,
        'comments': comments,
    }

    return render(request, 'news/news_detail.html', params)


class CommentCreateView(CreateView):
    pass