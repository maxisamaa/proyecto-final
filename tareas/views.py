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
    login_url = '/login/'
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
from datetime import date, timedelta,datetime
from django.contrib.auth.decorators import login_required



from django.shortcuts import render
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def vida_en_semanas(request):
    perfil = request.user.perfil

    # Si el usuario envía una fecha nueva → guardarla
    if request.method == "POST":
        fecha_str = request.POST.get("fecha_nacimiento")
        if fecha_str:
            perfil.fecha_nacimiento = date.fromisoformat(fecha_str)
            perfil.save()

    # Si NO tiene fecha → mostrar solo formulario
    if not perfil.fecha_nacimiento:
        return render(request, 'semanas.html')

    # Si SÍ tiene fecha → generar grilla
    fecha_nacimiento = perfil.fecha_nacimiento
    fecha_actual = date.today()
    total_anios = 100  # años que quieres mostrar
    semanas_por_ano = 52

    # Crear grilla: lista de listas (cada fila = un año con 52 semanas)
    grilla = []
    for anio in range(total_anios):
        fila = []
        for semana in range(semanas_por_ano):
            numero_semana = anio * semanas_por_ano + semana
            inicio_semana = fecha_nacimiento + timedelta(weeks=numero_semana)
            vivida = inicio_semana <= fecha_actual
            fila.append({'numero': numero_semana+1, 'vivida': vivida})
        grilla.append(fila)

    context = {
        'grilla': grilla,
        'total_anios': total_anios,
        'semanas_por_ano': semanas_por_ano,
    }

    return render(request, 'semanas.html', context)

