"""isur2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import comments
from isur2 import settings
from social.views import *

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^blog/$', BlogListView.as_view(), name='blog'),
    url(r'^news/$', NewsListView.as_view(), name='news'),
    # url(r'^news/get/(?P<pk>[0-9]+)$', NewsDetailView.as_view(), name='get_news'),
    url(r'^news/(?P<id>[0-9]+)$', add_news_comment, name='get_news'),
    url(r'^blog/get/(?P<pk>[0-9]+)$', BlogDetailView.as_view(), name='get_blog'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()
