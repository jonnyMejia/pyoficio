# -*- coding: utf-8 -*-
"""
Vistas de la aplicación globales
"""

# Django Library
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView, TemplateView

# Localfolder Library
from ..models import PyUser

class pylogin(TemplateView):
    template_name='usercustom/login.html'

##############################################################################
class SignUpView(TemplateView):
    """Esta clase sirve registrar a los usuarios en el sistema
    """
    model = PyUser
    template_name = 'usercustom/signup.html'
    extra_context = {}
    success_url = 'PyUser:login'
    success_message = _('Your account was created successfully. A link was sent to your email that you must sign in to confirm your sign up.')