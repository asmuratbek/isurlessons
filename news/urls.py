from django.conf.urls import url

from social.views import success_news

urlpatterns = [
    url(r'^created/$', success_news, name='news')
]