from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import comments
from isur2 import settings
from social.views import *

urlpatterns = [
    url(r'^news/(?P<id>[0-9])', add_news_comment, name='get_news'),
]