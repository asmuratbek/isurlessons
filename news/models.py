# coding=utf-8
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=225, verbose_name='Заголовок новости')
    image = models.ImageField(upload_to='images/news/', verbose_name='Изображение новости')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True)
    text = RichTextUploadingField(verbose_name='Текст новости')
    preview = models.TextField(max_length=255, verbose_name='Анонс новости')


    def __unicode__(self):
        return self.title