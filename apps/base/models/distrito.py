# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library

DISTRICT_CHOICE = (
    ("ANCON", "ANCON"),
    ('ATE', 'ATE'),
    ('BARRANCO', 'BARRANCO'),
    ('BREÑA', 'BREÑA'),
    ('CARABAYLLO', 'CARABAYLLO'),
    ('CHACLACAYO', 'CHACLACAYO'),
    ('CHORRILLOS', 'CHORRILLOS'),
    ('CIENEGUILLA', 'CIENEGUILLA'),
    ('COMAS', 'COMAS'),
    ('EL AGUSTINO', 'EL AGUSTINO'),
    ('INDEPENDENCIA', 'INDEPENDENCIA'),
    ('JESUS MARIA', 'JESUS MARIA'),
    ('LA MOLINA', 'LA MOLINA'),
    ('LA VICTORIA', 'LA VICTORIA'),
    ('LIMA', 'LIMA'),
    ('LINCE', 'LINCE'),
    ('LOS OLIVOS', 'LOS OLIVOS'),
    ('LURIGANCHO', 'LURIGANCHO'),
    ('LURIN', 'LURIN'),
    ('MAGDALENA DEL MAR', 'MAGDALENA DEL MAR'),
    ('MIRAFLORES', 'MIRAFLORES'),
    ('PACHACAMAC', 'PACHACAMAC'),
    ('MIRAFLORES', 'MIRAFLORES'),
    ('PUCUSANA', 'PUCUSANA'),
    ('PUEBLO LIBRE', 'PUEBLO LIBRE'),
    ('PUENTE PIEDRA', 'PUENTE PIEDRA'),
    ('PUNTA HERMOSA', 'PUNTA HERMOSA'),
    ('PUNTA NEGRA', 'PUNTA NEGRA'),
    ('RIMAC', 'RIMAC'),
    ('SAN BARTOLO', 'SAN BARTOLO'),
    ('SAN BORJA', 'SAN BORJA'),
    ('SAN ISIDRO', 'SAN ISIDRO'),
    ('SAN JUAN DE LURIGANCHO', 'SAN JUAN DE LURIGANCHO'),
    ('SAN JUAN DE MIRAFLORES', 'SAN JUAN DE MIRAFLORES'),
    ('SAN LUIS', 'SAN LUIS'),
    ('SAN MARTIN DE PORRES', 'SAN MARTIN DE PORRES'),
    ('SAN MIGUEL', 'SAN MIGUEL'),
    ('SANTA ANITA', 'SANTA ANITA'),
    ('SANTA ROSA', 'SANTA ROSA'),
    ('SANTIAGO DE SURCO', 'SANTIAGO DE SURCO'),
    ('SURQUILLO', 'SURQUILLO'),
    ('VILLA EL SALVADOR', 'VILLA EL SALVADOR'),
    ('VILLA MARIA DEL TRIUNFO', 'VILLA MARIA DEL TRIUNFO'),
)

class PyDistrito(models.Model):
    nombre= models.CharField(_("Nombre"), choices=DISTRICT_CHOICE, max_length=64, default='LIMA')
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("Distrito")
        verbose_name_plural = _("Distritos")
