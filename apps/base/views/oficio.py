# Django Library
from django.views.generic import TemplateView, DetailView, ListView
from django.db.models import Count

# Localfolder Library 
from ..models import PyOficio, PyUser, PyProduct

class OficioList(TemplateView):
    template_name = "home/oficio_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(OficioList, self).get_context_data(**kwargs)
        context["oficios"] = PyOficio.objects.annotate(cantidad=Count('usuario'))
        return context


class OficioDetail(DetailView):
    template_name = "home/oficio_detail.html"
    model = PyOficio

