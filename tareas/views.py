from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea 
from tareas.forms import TareaForm 
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

class ListaTareas(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'lista.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = Tarea.objects.filter(usuario=self.request.user)

        # Orden según GET
        orden = self.request.GET.get("orden")
        if orden == "tipo":
            queryset = queryset.order_by("tipo__nombre")
        elif orden == "proximidad":
            queryset = queryset.order_by("proximidad__valor")
        elif orden == "prioridad":
            queryset = queryset.order_by("prioridad__orden")
        else:
            # Orden por defecto si no hay GET
            queryset = queryset.order_by('fecha_termino')

        return queryset


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = 'formulario.html'
    form_class = TareaForm
    success_url = reverse_lazy('lista_tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna dueño
        return super().form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name = 'formulario.html'
    form_class = TareaForm
    success_url = reverse_lazy('lista_tareas')

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar.html'
    success_url = reverse_lazy('lista_tareas')

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'detalle.html'
    context_object_name = 'tarea'

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)
    


######### grilla

from django.shortcuts import render
from datetime import date, timedelta

def vida_en_semanas(request):
    # Reemplaza con tu fecha de nacimiento
    fecha_nacimiento = date(1995, 7, 26)  
    fecha_actual = date.today()
    semanas_totales = 100 * 52  # 100 años x 52 semanas aprox

    semanas = []
    for semana_num in range(semanas_totales):
        inicio_semana = fecha_nacimiento + timedelta(weeks=semana_num)
        vivida = inicio_semana <= fecha_actual
        semanas.append({
            'numero': semana_num,
            'vivida': vivida
        })

    return render(request, 'semanas.html', {'semanas': semanas})
