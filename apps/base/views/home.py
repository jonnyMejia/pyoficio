# Django Library
from django.contrib.auth.decorators import login_required
from . import TemplateView

# Localfolder Library 

class Oficio_home(TemplateView):
    template_name = "home.html"
    
