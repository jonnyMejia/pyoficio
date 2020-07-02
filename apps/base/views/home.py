# -*- coding: utf-8 -*-
"""
Vista del home
"""

# Django Library
from django.views.generic import RedirectView, TemplateView

class oficio_home(TemplateView):
    template_name='home.html'


