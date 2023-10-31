from django.views.generic import TemplateView
from django.conf import settings

class Index(TemplateView):
    template_name = 'index.html'
