# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u0446 \u0438\u043a\u043e\u043d\u043a\u0438', max_length=60, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('f_link', models.CharField(blank=True, max_length=225, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u0435\u0439\u0441\u0431\u0443\u043a')),
                ('t_link', models.CharField(blank=True, max_length=225, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0442\u0432\u0438\u0442\u0442\u0435\u0440')),
                ('i_link', models.CharField(blank=True, max_length=225, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0438\u043d\u0441\u0442\u0430\u0433\u0440\u0430\u043c\u043c')),
                ('y_link', models.CharField(blank=True, max_length=225, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u044e\u0442\u0443\u0431')),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0435\u0442\u044c',
                'verbose_name_plural': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438',
            },
        ),
    ]
