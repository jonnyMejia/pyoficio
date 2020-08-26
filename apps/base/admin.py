"""
Sección administrativa
"""
# Django Library
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

# Localfolder Library
from .forms import PersonaChangeForm, PersonaCreationForm
from .models import (
    PyUser, PyProduct, PyDistrito, PyOficio)

class PersonaAdmin(UserAdmin):
    """ Admin para usuarios
    """
    search_fields = ('email',)
    list_filter = ('is_active',)
    list_display = ('__str__', 'email',)
    # list_select_related = ()
    show_full_result_count = False
    actions_selection_counter = False
    ordering = ('id',)
    # Definir fieldsets ya que "username" se establece por defecto y no debe ir
    fieldsets =  (
        (None, {'fields': ('email','password',)}),
        ('Informacion Personal', {'fields': ('first_name','last_name','distrito','celular','avatar')}),
        ('Permisos', {'fields': ('is_active','is_staff','is_superuser','user_permissions',)}),
    )
    

admin.site.register(PyUser, PersonaAdmin)
admin.site.register(PyOficio)
admin.site.register(PyProduct)
admin.site.register(PyDistrito)
admin.site.register(LogEntry)