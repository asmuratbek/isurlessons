# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse

from blog.models import Blog
from news.models import News


class CommentsBlog(models.Model):
    class Meta:
        verbose_name =  'Комментарий блога'
        verbose_name_plural = 'Коментарии блога'

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Статья')
    date = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=255, verbose_name='Email')
    text = models.TextField(verbose_name='Text')

    def __unicode__(self):
        return self.email



class CommentsNews(models.Model):
    class Meta:
        verbose_name = 'Комментарий новости'
        verbose_name_plural = 'Коментарии новостей'

    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')
    date = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=255, verbose_name='Email')
    text = models.TextField(verbose_name='Text')

    def __unicode__(self):
        return self.email
