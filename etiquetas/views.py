from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Etiqueta

class lista_etiquetas(LoginRequiredMixin, ListView):
    model = Etiqueta
    template_name = 'lista2.html'
    context_object_name = 'etiquetas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        etiquetas = context['etiquetas']
        tareas_usuario = self.request.user.tarea_set.all()

        # Lista de tuplas (etiqueta, tareas_filtradas)
        context['etiquetas_con_tareas'] = [
            (etiqueta, tareas_usuario.filter(etiquetas=etiqueta))
            for etiqueta in etiquetas
        ]

        return context

class crear_etiqueta(LoginRequiredMixin,CreateView):
    model = Etiqueta
    template_name = 'formulario2.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_etiquetas')

class editar_etiqueta(LoginRequiredMixin,UpdateView):
    model = Etiqueta
    template_name = 'formulario2.html'
    fields = ['nombre']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('lista_etiquetas')

class eliminar_etiqueta(LoginRequiredMixin,DeleteView):
    model = Etiqueta
    template_name = 'borrar.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('lista_etiquetas')