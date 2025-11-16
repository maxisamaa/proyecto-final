from django.shortcuts import render, get_object_or_404, redirect
from .models import Referencias, Pensamientos
from .forms import ReferenciasForm, PensamientosForm

# --- REFERENCIAS ---

def lista_referencias(request):
    referencias = Referencias.objects.all()
    pensamientos = Pensamientos.objects.all()
    return render(request, 'listita.html', {
        'referencias': referencias,
        'pensamientos': pensamientos,
    })

def crear_referencia(request):
    if request.method == 'POST':
        form = ReferenciasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_referencias')
    else:
        form = ReferenciasForm()
    return render(request, 'formulario_referencias.html', {'form': form})

def editar_referencia(request, id):
    referencia = get_object_or_404(Referencias, id=id)
    if request.method == 'POST':
        form = ReferenciasForm(request.POST, instance=referencia)
        if form.is_valid():
            form.save()
            return redirect('lista_referencias')
    else:
        form = ReferenciasForm(instance=referencia)
    return render(request, 'formulario_referencias.html', {'form': form})

def eliminar_referencia(request, id):
    referencia = get_object_or_404(Referencias, id=id)
    if request.method == 'POST':
        referencia.delete()
        return redirect('lista_referencias')
    return render(request, 'eliminar.html', {'obj': referencia})


# --- PENSAMIENTOS ---
def crear_pensamiento(request):
    if request.method == 'POST':
        form = PensamientosForm(request.POST)
        if form.is_valid():
            pensamiento = form.save(commit=False)
            pensamiento.autor = request.user  # asignar el usuario logueado
            pensamiento.save()
            form.save_m2m()
            return redirect('lista_referencias')
    else:
        form = PensamientosForm()
    return render(request, 'formulario_pensamientos.html', {'form': form})

def editar_pensamiento(request, id):
    pensamiento = get_object_or_404(Pensamientos, id=id)
    if request.method == 'POST':
        form = PensamientosForm(request.POST, instance=pensamiento)
        if form.is_valid():
            form.save()
            return redirect('lista_referencias')
    else:
        form = PensamientosForm(instance=pensamiento)
    return render(request, 'formulario_pensamientos.html', {'form': form})

def eliminar_pensamiento(request, id):
    pensamiento = get_object_or_404(Pensamientos, id=id)
    if request.method == 'POST':
        pensamiento.delete()
        return redirect('lista_referencias')
    return render(request, 'eliminar.html', {'obj': pensamiento})
