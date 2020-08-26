# Standard Library
import os

# Django Library
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..rename_image import RenameImage
from .usercustom import PyUser

_UNSAVED_FILEFIELD = 'unsaved_filefield'
DEFAULT_USER_ID = 1
def image_path(instance, filename):
    root, ext = os.path.splitext(filename)
    return "product/{id}{ext}".format(id=instance.pk, ext=ext)


PRODUCT_CHOICE = (
    ("product", "Almacenable"),
    ('consu', 'Consumible'),
    ('service', 'Servicio'),
    ('software', 'Software')
)


class PyProduct(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=80)
    costo = models.DecimalField(_("Costo/Precio"), max_digits=10, decimal_places=2, default=0)
    description = models.TextField(_("Descripcion"), blank=True, null=True)
    youtube_video = models.CharField(null=True, blank=True, max_length=300)
    img = models.ImageField(
        max_length=255,
        storage=RenameImage(),
        upload_to=image_path,
        blank=True,
        null=True,
        default='product/default_product.png'
    )
    dueño = models.ForeignKey(
        PyUser,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        default=DEFAULT_USER_ID,
        verbose_name=_('Usuario')
    )
    
    type = models.CharField(_("Tipo"), choices=PRODUCT_CHOICE, max_length=64, default='consu')

    def __str__(self):
        return format(self.nombre)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


@receiver(pre_save, sender=PyProduct)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.img)
        instance.img = 'product/default_product.png'

@receiver(post_save, sender=PyProduct)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.img = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
    if not instance.img or instance.img is None:
        instance.img = 'product/default_product.png'
        instance.save()
