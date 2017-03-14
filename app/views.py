# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import uuid
from app.models import File
from common.utils import Utils
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.core.files.base import ContentFile
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.storage import staticfiles_storage


@method_decorator(csrf_exempt, name='dispatch')
class MediaUploadView(View):
    def post(self, request):
        uploaded_file = ContentFile(request.body)
        uploaded_file.name = "%s.%s" % (uuid.uuid4(), 'png')
        file = File(location=uploaded_file)
        file.save()

        return HttpResponse(Utils.media_url(file.location.name))


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Django Webcam'
        return context
