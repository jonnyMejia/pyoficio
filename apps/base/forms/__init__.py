# -*- coding: utf-8 -*-
"""
Formularios para la app globales
"""
# Standard Library
import re

# Django Library
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library

# Localfolder Library
from ..models import PyUser

from .producto import ProductoForm
from .usercustom import ProfileForm

class PersonaChangeForm(UserChangeForm):
    """Para algo sera esto
    """
    class Meta(UserChangeForm.Meta):
        model = PyUser
        fields = (
            'email',
            'is_active',
            'last_login',
            'first_name',
            'last_name',
        )

class PersonaCreationForm(UserCreationForm):
    """Con esta clase de formulario se renderiza la plantilla de registro de
    ususarios
    """
    class Meta(UserCreationForm.Meta):
        model = PyUser
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': _('Email')}
            ),
        }




