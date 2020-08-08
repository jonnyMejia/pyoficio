"""uRLs para base
"""
# Django Library
from django.urls import path, include

# Localfolder Library
from ..views import Oficio_home

urlpatterns = [
    path('',Oficio_home.as_view(),name = 'home'),
    path('', include('apps.base.urls.usercustom')),
]