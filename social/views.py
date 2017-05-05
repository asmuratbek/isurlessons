# coding=utf-8
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.models import Blog
from comments.forms import CommentBlogForm
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


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = CommentsBlog.objects.all()
        context['form'] = CommentBlogForm
        return context

    def post(self, request, *args, **kwargs):
        if request.POST:
            form = CommentBlogForm(request.POST)
            if form.is_valid():
                comment = CommentsBlog()
                comment.email = form.cleaned_data['email']
                comment.blog = self.get_object()
                comment.text = form.cleaned_data['text']
                comment.save()
                messages.success(request, 'Your profile was updated.')

                return HttpResponseRedirect('/blog/get/%s' % self.get_object().id )

        return JsonResponse(dict(success=True))


class NewsListView(BlogListView):
    model = News


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['comments'] = CommentsNews.objects.all()

        return context

