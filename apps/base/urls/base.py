"""uRLs para base
"""
# Django Library
from django.urls import path
from django.conf.urls import url

# Localfolder Library

from ..views.dashboard import  Dashboard, Profile, ProductoUpdate, ProductoCreate, ProductoDelete

app_name = 'base'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    url(r'^profile/(?P<pk>\d+)', Profile.as_view(), name='profile'),
    path('product/<int:pk>/update', ProductoUpdate.as_view(), name='update'),
    path('product/<int:pk>/delete', ProductoDelete.as_view(), name='delete'),
    path('product/create', ProductoCreate.as_view(), name='create'),

]