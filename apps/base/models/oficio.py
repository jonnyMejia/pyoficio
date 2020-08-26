# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .usercustom import PyUser

class PyOficio(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=80)
    usuario = models.ManyToManyField(
        PyUser,
        verbose_name=_('Usuarios')
    )
    class Meta:
        verbose_name = _("Oficio")
        verbose_name_plural = _("Oficios")