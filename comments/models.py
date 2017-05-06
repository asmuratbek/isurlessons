# coding=utf-8
from __future__ import unicode_literals
from blog.models import Author

from django.db import models


# Create your models here.
from news.models import News


class CommentsBlog(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField(max_length=300, verbose_name='Текст комментария')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True)
    activity = models.BooleanField()

    def __unicode__(self):
        return self.text


class CommentsNews(models.Model):
    class Meta:
        verbose_name = 'N.Комментарий'
        verbose_name_plural = 'N.Комментарии'
    newscomment= models.ForeignKey(title.News, on_delete=models.CASCADE())
    text = models.TextField(max_length=300, verbose_name='Текст комментария')
    theme = models.ForeignKey(News, on_delete=models.CASCADE, null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True)
    activity = models.BooleanField()

    def __unicode__(self):
        return self.text
