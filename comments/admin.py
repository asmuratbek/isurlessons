from django.contrib import admin
from .models import *


# Register your models here.
class CommentsBlogAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')


admin.site.register(CommentsBlog, CommentsBlogAdmin)



class CommentsNewsAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')


admin.site.register(CommentsNews, CommentsNewsAdmin)
