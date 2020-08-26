# Django Library
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url
from django.urls import path, include,re_path
from django.contrib import admin

# Thirty Library
from rest_auth.registration.views import VerifyEmailView, RegisterView

# Localfolder Library

urlpatterns = [
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    url('', include('allauth.urls')),
]

