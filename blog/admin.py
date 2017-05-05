from django.contrib import admin
from jet.filters import RelatedFieldAjaxListFilter

from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'image', 'preview', 'text')
    list_display = ('title', 'author')
    # list_filter = (
    #     ('blog', RelatedFieldAjaxListFilter),
    # )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)