# -*- coding: utf-8
"""
Modelo de datos de la app globales
"""
# Standard Library
import os

# Django Library
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from . import PyUserManager, PyDistrito
from ..rename_image import RenameImage


def image_path(instance, filename):
    return os.path.join('avatar', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])

class PyUser(AbstractUser):
    '''Modelo de los usuarios
    '''
    username = None
    email = models.EmailField(_("Email"), max_length=254, null=False, db_index=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PyUserManager()

    first_name = models.CharField(_("Nombres"), max_length=30)
    last_name = models.CharField(_("Apellidos"), max_length=30, blank=True, null=True)
    
    distrito = models.ForeignKey(
        PyDistrito,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Distrito')
    )
    
    celular = models.CharField(_("Numero Móvil"), max_length=255, blank=True, null=True)
    avatar = models.ImageField(max_length=255, storage=RenameImage(), upload_to=image_path, blank=True, null=True, default='avatar/default_avatar.png')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
