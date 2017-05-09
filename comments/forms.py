from django import forms

from comments.models import CommentsBlog, CommentsNews


class CommentBlogForm(forms.Form):
    email = forms.CharField()
    text = forms.CharField()
    blog = forms.IntegerField()

class CommentNewsForm(forms.ModelForm):
    class Meta:
        model = CommentsNews
        # exclude = ['news',]
        fields = ['email','text',]

