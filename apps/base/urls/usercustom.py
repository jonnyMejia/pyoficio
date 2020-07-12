# Django Library
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

# Thirty Library
from rest_auth.registration.views import VerifyEmailView, RegisterView

# Localfolder Library
from ..views import Oficio_home

urlpatterns = [
    #path('',Oficio_home.as_view(),name = 'home'),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    path('', include('rest_auth.urls')),
    path('signup/', include('rest_auth.registration.urls')),
]

