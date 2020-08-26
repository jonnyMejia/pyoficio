"""uRLs para base
"""
# Django Library
from django.urls import path, include

# Localfolder Library
from ..views import Oficio_home, OficioDetail, OficioList

urlpatterns = [
    path('', Oficio_home.as_view(),name = 'home'),
    path('oficio/', OficioList.as_view(),name = 'oficio_list'),
    path('oficio/<int:pk>/', OficioDetail.as_view(),name = 'oficio_detail'),
    path('contacto/', Oficio_home.as_view(),name = 'contacto'),
    path('', include('apps.base.urls.usercustom')),
]