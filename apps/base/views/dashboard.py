# Django Library
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from . import TemplateView


# Localfolder Library 

@login_required()
def oficio_dashboard(request):
    """Vista para renderizar el dasboard del oficio
    """
    return render(request, "base/dashboard.html")



