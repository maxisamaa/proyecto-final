from django.shortcuts import render, get_object_or_404, redirect
from .models import Referencias, Pensamientos
from .forms import ReferenciasForm, PensamientosForm
from django.contrib.auth.decorators import login_required

# --- REFERENCIAS ---
@login_required(login_url='/login/')
def lista_referencias(request):
    referencias = Referencias.objects.filter(usuario=request.user)
    pensamientos = Pensamientos.objects.filter(usuario=request.user)
    return render(request, 'listita.html', {
        'referencias': referencias,
        'pensamientos': pensamientos,
    })
@login_required(login_url='/login/')
def crear_referencia(request):
    if request.method == 'POST':
        form = ReferenciasForm(request.POST)
        if form.is_valid():
            referencia = form.save(commit=False)
            referencia.usuario = request.user  # asigna el usuario logueado
            referencia.save()
            form.save_m2m()
            return redirect('lista_referencias')
    else:
        form = ReferenciasForm()
    return render(request, 'formulario_referencias.html', {'form': form})

@login_required(login_url='/login/')
def editar_referencia(request, id):
    referencia = get_object_or_404(Referencias, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ReferenciasForm(request.POST, instance=referencia)
        if form.is_valid():
            form.save()
            return redirect('lista_referencias')
    else:
        form = ReferenciasForm(instance=referencia)
    return render(request, 'formulario_referencias.html', {'form': form})

@login_required(login_url='/login/')
def eliminar_referencia(request, id):
    referencia = get_object_or_404(Pensamientos, id=id, usuario=request.user)
    if request.method == 'POST':
        referencia.delete()
        return redirect('lista_referencias')
    return render(request, 'eliminar.html', {'obj': referencia})


# --- PENSAMIENTOS ---
@login_required(login_url='/login/')
def crear_pensamiento(request):
    if request.method == 'POST':
        form = PensamientosForm(request.POST)
        if form.is_valid():
            pensamiento = form.save(commit=False)
            pensamiento.usuario = request.user  # asigna el usuario logueado
            pensamiento.save()
            form.save_m2m()
            return redirect('lista_referencias')
    else:
        form = PensamientosForm()
    return render(request, 'formulario_pensamientos.html', {'form': form})

@login_required(login_url='/login/')
def editar_pensamiento(request, id):
    pensamiento = get_object_or_404(Pensamientos, id=id, usuario=request.user)
    if request.method == 'POST':
        form = PensamientosForm(request.POST, instance=pensamiento)
        if form.is_valid():
            form.save()
            return redirect('lista_referencias')
    else:
        form = PensamientosForm(instance=pensamiento)
    return render(request, 'formulario_pensamientos.html', {'form': form})

@login_required(login_url='/login/')
def eliminar_pensamiento(request, id):
    pensamiento = get_object_or_404(Pensamientos, id=id, usuario=request.user)
    if request.method == 'POST':
        pensamiento.delete()
        return redirect('lista_referencias')
    return render(request, 'eliminar.html', {'obj': pensamiento})


@login_required(login_url='/login/')
def ver_referencia(request, id):
    referencia = get_object_or_404(Referencias, id=id, usuario=request.user)
    return render(request, 'detalles_referencia.html', {'referencia': referencia})

@login_required(login_url='/login/')
def ver_pensamiento(request, id):
    pensamiento = get_object_or_404(Pensamientos, id=id, usuario=request.user)
    return render(request, 'detalles_pensamiento.html', {'pensamiento': pensamiento})
