# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from urllib.parse import urljoin


class Utils:
    @staticmethod
    def url(path):
        return urljoin(settings.APP_URL, path)

    @staticmethod
    def static_url(path):
        return urljoin(Utils.url(settings.STATIC_URL), path)

    @staticmethod
    def media_url(path):
        return urljoin(Utils.url(settings.MEDIA_URL), path)
