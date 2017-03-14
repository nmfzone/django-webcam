# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from app.views import IndexView, MediaUploadView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^upload/$', MediaUploadView.as_view(), name='media_upload')
]
