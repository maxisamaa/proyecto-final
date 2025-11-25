from django.shortcuts import render
from categorias.models import Tipo, Proximidad, Prioridad
from django.contrib.auth.decorators import login_required
from tareas.models import Tarea

@login_required(login_url='/login/')
def categorias_panel(request):
    tareas_usuario = Tarea.objects.filter(usuario=request.user)

    tipos = Tipo.objects.all()
    proximidades = Proximidad.objects.all()
    prioridades = Prioridad.objects.all()

    # Agregar atributo dinámico a cada categoría
    for tipo in tipos:
        tipo.tareas_usuario = tareas_usuario.filter(tipo=tipo)

    for prox in proximidades:
        prox.tareas_usuario = tareas_usuario.filter(proximidad=prox)

    for prio in prioridades:
        prio.tareas_usuario = tareas_usuario.filter(prioridad=prio)

    context = {
        'tipos': tipos,
        'proximidades': proximidades,
        'prioridades': prioridades,
    }

    return render(request, 'menu.html', context)

