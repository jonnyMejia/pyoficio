"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

from django.conf.urls import url
from django.urls import path, include, re_path
from django.contrib import admin

# Thirty Library
from allauth.account.views import confirm_email


urlpatterns = [
    # ============================ New URLs ============================ #
    path('', include('apps.base.urls.home')),
    path('base/', include('apps.base.urls.base')),
]