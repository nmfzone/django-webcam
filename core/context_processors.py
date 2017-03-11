# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings


def settings_context_processor(request):
    """
    Expose django settings to template engine
    """
    parsed_settings = {
        'APP_VERSION': settings.APP_VERSION,
        'APP_NAME': settings.APP_NAME,
    }

    return {
        'SETTINGS': parsed_settings,
    }
