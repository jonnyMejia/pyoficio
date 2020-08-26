# -*- coding: utf-8 -*-
"""
Formularios
"""
# Django Library
from django import forms
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library

# Localfolder Library
from ..models import PyDistrito, PyProduct, PyUser       

class ProfileForm(forms.ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """
    class Meta:
        model = PyUser
        fields = (
            'first_name',
            'last_name',
            'celular',
            'distrito',
            'avatar',
        )
        labels = {
            'first_name': _('Name'),
            'last_name': _('Last Name'),
            'celular': _('Mobile Phone'),
            'distrito': _('Distrito'),
            'avatar': _('Foto de Perfil'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.Select(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }