from django.conf.urls import url

from social.views import success_blog

urlpatterns = [
    url(r'^created/$', success_blog, name='blog')
]