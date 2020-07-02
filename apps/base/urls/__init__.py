"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # ============================ New URLs ============================ #
    path('', include('apps.base.urls.usercustom')),
    path('base/', include('apps.base.urls.base')),
]