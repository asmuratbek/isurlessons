from django import forms

from comments.models import CommentsBlog


class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = CommentsBlog
        exclude = ['blog',]

