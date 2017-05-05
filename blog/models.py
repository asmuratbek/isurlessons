# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"

    title = models.CharField(max_length=255, verbose_name='Название статьи')
    image = models.ImageField(upload_to='images/blog/', verbose_name='Изображение статьи')
    date = models.DateTimeField(auto_now_add=True, null=True)
    preview = models.TextField(max_length=255, verbose_name='Анонс статьи')
    text = models.TextField(verbose_name='Текст статьи')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    @staticmethod
    def autocomplete_search_fields():
        return 'title', 'author'



    def __unicode__(self):
        return self.title

class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural =  'Авторы'

    name = models.CharField(max_length=100, verbose_name='Имя автора')

    def __unicode__(self):
        return self.name