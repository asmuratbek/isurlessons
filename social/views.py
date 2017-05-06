from django.shortcuts import render

from blog.models import Blog
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


def get_news(request, id):
    news = News.objects.filter(id=id).first()

    params = {
        'news' : news,
    }

    return render(request, 'detail.html', params)

def get_blog(request, id):
    blog = Blog.objects.filter(id=id).first()

    params = {
        'blog' : blog,
    }

    return render(request, 'detail.html', params)
