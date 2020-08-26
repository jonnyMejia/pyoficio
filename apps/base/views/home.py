# Django Library
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Q
# Localfolder Library 
from ..models import PyOficio, PyUser, PyProduct

class Oficio_home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super(Oficio_home, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q :
            context["productos"] = PyProduct.objects.filter(Q(nombre__icontains = q))
        else:
            context["productos"] = PyProduct.objects.all()
        return context
    
    
