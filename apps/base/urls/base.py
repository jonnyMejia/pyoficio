"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from django.urls import path
from ..views.dashboard import oficio_dashboard

app_name = 'base'

urlpatterns = [
    path('', oficio_dashboard, name='dashboard'),
]