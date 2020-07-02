"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from django.urls import path
from ..views.home import oficio_home

app_name = 'base'

urlpatterns = [
    path('', oficio_home, name='home'),
]