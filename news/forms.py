from django.forms import ModelForm
from news.models import News


class CreateNews(ModelForm):
    class Meta:
        model = News
        exclude = ['date']
        # fields = ['title', 'image', 'preview', 'text']