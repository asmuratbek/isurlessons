# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class SocialLinks(models.Model):
    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    title = models.CharField(max_length=60, verbose_name='Название', default='Редактировать соц иконки')
    f_link = models.CharField(max_length=225, verbose_name='Ссылка на фейсбук', null=True, blank=True)
    t_link = models.CharField(max_length=225, verbose_name='Ссылка на твиттер', null=True, blank=True)
    i_link = models.CharField(max_length=225, verbose_name='Ссылка на инстаграмм', null=True, blank=True)
    y_link = models.CharField(max_length=225, verbose_name='Ссылка на ютуб', null=True, blank=True)
