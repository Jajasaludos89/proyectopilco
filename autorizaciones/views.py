from django.shortcuts import render, get_object_or_404, redirect
from .models import Autorizacion,Proyecto,Municipio,Condicion
from .forms import AutorizacionForm, ProyectoForm,MunicipioForm,CondicionForm

# Listar autorizaciones
def lista_autorizaciones(request):
    autorizaciones = Autorizacion.objects.all()
    return render(request, 'autorizaciones/lista.html', {'autorizaciones': autorizaciones})

# Crear una nueva autorización
def crear_autorizacion(request):
    if request.method == 'POST':
        form = AutorizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizaciones')
    else:
        form = AutorizacionForm()
    return render(request, 'autorizaciones/formulario.html', {'form': form})

# Editar una autorización
def editar_autorizacion(request, pk):
    autorizacion = get_object_or_404(Autorizacion, pk=pk)
    if request.method == 'POST':
        form = AutorizacionForm(request.POST, instance=autorizacion)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizaciones')
    else:
        form = AutorizacionForm(instance=autorizacion)
    return render(request, 'autorizaciones/formulario.html', {'form': form})

# Eliminar una autorización
def eliminar_autorizacion(request, pk):
    autorizacion = get_object_or_404(Autorizacion, pk=pk)
    if request.method == 'POST':
        autorizacion.delete()
        return redirect('lista_autorizaciones')
    return render(request, 'autorizaciones/confirmar_eliminar.html', {'autorizacion': autorizacion})


# Listar proyectos
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/proyecto_lista.html', {'proyectos': proyectos})

# Crear proyecto
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/proyecto_formulario.html', {'form': form})


# Editar proyecto
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto/proyecto_formulario.html', {'form': form})


# Aprobar proyecto
def aprobar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    try:
        proyecto.aprobar()
        return redirect('lista_proyectos')
    except ValueError as e:
        return render(request, 'proyecto/error_aprobacion.html', {'error': str(e)})


# Eliminar proyecto
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'proyecto/confirmar_eliminar.html', {'proyecto': proyecto})


# Lista de municipios
def lista_municipios(request):
    municipios = Municipio.objects.all()
    return render(request, 'municipio/municipio_lista.html', {'municipios': municipios})

# Crear municipio
def crear_municipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_municipios')
    else:
        form = MunicipioForm()
    return render(request, 'municipio/municipio_formulario.html', {'form': form})

# Editar municipio
def editar_municipio(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == 'POST':
        form = MunicipioForm(request.POST, instance=municipio)
        if form.is_valid():
            form.save()
            return redirect('lista_municipios')
    else:
        form = MunicipioForm(instance=municipio)
    return render(request, 'municipio/municipio_formulario.html', {'form': form})

# Eliminar municipio
def eliminar_municipio(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == 'POST':
        municipio.delete()
        return redirect('lista_municipios')
    return render(request, 'municipio/confirmar_eliminar.html', {'municipio': municipio})


# Lista de condiciones
def lista_condiciones(request):
    condiciones = Condicion.objects.all()
    return render(request, 'condiciones/condicion_lista.html', {'condiciones': condiciones})

# Crear condición
def crear_condicion(request):
    if request.method == 'POST':
        form = CondicionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_condiciones')
    else:
        form = CondicionForm()
    return render(request, 'condiciones/condicion_formulario.html', {'form': form})

# Editar condición
def editar_condicion(request, pk):
    condicion = get_object_or_404(Condicion, pk=pk)
    if request.method == 'POST':
        form = CondicionForm(request.POST, instance=condicion)
        if form.is_valid():
            form.save()
            return redirect('lista_condiciones')
    else:
        form = CondicionForm(instance=condicion)
    return render(request, 'condiciones/condicion_formulario.html', {'form': form})

# Eliminar condición
def eliminar_condicion(request, pk):
    condicion = get_object_or_404(Condicion, pk=pk)
    if request.method == 'POST':
        condicion.delete()
        return redirect('lista_condiciones')
    return render(request, 'condiciones/confirmar_eliminar.html', {'condicion': condicion})

