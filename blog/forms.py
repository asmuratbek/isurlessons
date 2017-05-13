from django.forms import ModelForm

from blog.models import Blog


class CreateBlog(ModelForm):
    class Meta:
        model = Blog
        exclude = ['date']