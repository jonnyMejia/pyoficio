# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DeleteView
from django.views.generic.edit import FormMixin, UpdateView, CreateView
from django.urls import reverse_lazy


from ..forms import  ProfileForm, ProductoForm


# Localfolder Library 
from ..models import PyUser, PyProduct

class Dashboard(LoginRequiredMixin, TemplateView):

    model = PyUser
    template_name = "base/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['productos'] = PyProduct.objects.all()
        return context
    
class ProductoUpdate(UpdateView):
    model = PyProduct
    template_name = 'base/producto_update.html'
    form_class = ProductoForm

    def get_success_url(self):
        return reverse_lazy('base:update', kwargs={'pk': self.object.pk})

    def get_object(self):
        try:
            my_object = PyProduct.objects.get(id=self.kwargs.get('pk'))
            return my_object
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
    

class ProductoCreate(CreateView):
    model = PyProduct
    template_name = 'base/producto_create.html'
    form_class = ProductoForm

    def form_valid(self, form):
        producto = form.save()
        producto.dueño = self.request.user
        producto.save()
        return super(ProductoCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('base:update', kwargs={'pk': self.object.pk})

class ProductoDelete(DeleteView):
    model = PyProduct
    template_name='base/producto_delete.html'
    success_url ="/base"

class Profile(UpdateView):

    model = PyUser
    template_name = 'base/profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('base:profile', kwargs={'pk': self.object.pk})

    def get_object(self):
        try:
            my_object = PyUser.objects.get(id=self.kwargs.get('pk'))
            return my_object
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

    