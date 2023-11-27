from django.views.generic import TemplateView
from django.conf import settings

class Lector(TemplateView):
    template_name = 'lector.html'
    
