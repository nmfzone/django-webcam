from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView as View


class IndexView(View):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'This is just the beginning'
        return context
