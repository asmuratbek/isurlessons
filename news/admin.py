from django.contrib import admin

from .models import *
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    fields = ('title','image','preview', 'text')
    list_display = ('title', 'preview')


admin.site.register(News, NewsAdmin)