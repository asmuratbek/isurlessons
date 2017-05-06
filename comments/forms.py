from django import forms

from comments.models import CommentsBlog, CommentsNews


class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = CommentsBlog
        exclude = ['blog',]

class CommentNewsForm(forms.ModelForm):
    class Meta:
        model = CommentsNews
        # exclude = ['news',]
        fields = ['email','text',]

