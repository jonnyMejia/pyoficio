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

class ProductoForm(forms.ModelForm):
    """Fromulario para los productos
    """

    class Meta:
        model = PyProduct
        fields = [
            'nombre',
            'costo',
            'description',
            'youtube_video',
            'img',
            'type',
        ]
        labels = {
            'nombre': _('Nombre'),
            'costo': _('Precio'),
            'description': _('Descripcion'),
            'youtube_video': _('Youtube URL'),
            'img': _('Imagen'),
            'type': _('Tipo de producto'),
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'youtube_video': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }