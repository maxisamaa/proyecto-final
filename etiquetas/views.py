from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Etiqueta

class lista_etiquetas(ListView):
    model = Etiqueta
    template_name = 'lista2.html'
    context_object_name = 'etiquetas'

class crear_etiqueta(CreateView):
    model = Etiqueta
    template_name = 'formulario2.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_etiquetas')

class editar_etiqueta(UpdateView):
    model = Etiqueta
    template_name = 'formulario2.html'
    fields = ['nombre']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('lista_etiquetas')

class eliminar_etiqueta(DeleteView):
    model = Etiqueta
    template_name = 'borrar.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('lista_etiquetas')