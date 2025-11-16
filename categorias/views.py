from django.shortcuts import render
from categorias.models import Tipo, Proximidad, Prioridad

def categorias_panel(request):
    context = {
        'tipos': Tipo.objects.all(),
        'proximidades': Proximidad.objects.all(),
        'prioridades': Prioridad.objects.all(),
    }
    return render(request, 'menu.html', context)