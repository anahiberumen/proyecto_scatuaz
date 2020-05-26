from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Trabajador, Actualizacion
from .forms import TrabajadorForm
from usuario.models import UserSCATUAZ
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


@login_required
def lista_trabajador(request):
    trabajadores = Trabajador.objects.all()
    query = request.GET.get('q')
    print('query is', query)
    if query:
        print('WE ARE IN')
        trabajadores = Trabajador.objects.filter(
            Q(nombre=query) | Q(paterno=query) | Q(materno=query) | Q(rfc=query)
        ).distinct()

    paginator = Paginator(trabajadores, 10)
    numero_pagina = request.GET.get('page')
    
    try:
        pagina = paginator.page(numero_pagina)
    except PageNotAnInteger:
        pagina = paginator.page(1)
    except EmptyPage:
        pagina = paginator.page(paginator.num_pages)

    context = {
        'actual': 'trabajador',
        'pagina': pagina,
    }
    return render(request, 'lista_trabajador.html', context)


@login_required
def ver_trabajador(request, id):
    trabajador = Trabajador.objects.get(pk=id)
    try:
        actualizaciones = Actualizacion.objects.filter(id_trabajador=id)
    except:
        actualizaciones = ()
    context = {
        'trabajador': trabajador,
        'actualizaciones': actualizaciones
    }

    return render(request, 'ver_trabajador.html', context)


@login_required
def agregar_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            tmp = form.save(commit=False)
            usuario = UserSCATUAZ.objects.get(pk=request.user.id)
            tmp.alta_usuario = usuario
            tmp.save()
            return redirect('lista_trabajador')
    else:
        form = TrabajadorForm()
    return render(request, 'agregar_trabajador.html', {'form': form})


@login_required
def eliminar_trabajador(request, pk):
    if request.method == 'POST':
        try:
            trabajador = Trabajador.objects.get(pk=pk)
            trabajador.delete()
            return redirect('lista_trabajador')
        except Trabajador.DoesNotExist:
            trabajadores = Trabajador.objects.all()
            context = {
                'trabajadores': trabajadores
            }
            return render(request, 'lista_trabajador.html', context)
    else:
        trabajador = Trabajador.objects.get(pk=pk)
        return render(request, 'confirm_delete.html', {'trabajador': trabajador})


@login_required
def modificar_trabajador(request, id):
    trabajador = Trabajador.objects.get(pk=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            Actualizacion.objects.create(
                id_trabajador=trabajador, usuario=request.user)
            return redirect('lista_trabajador')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'modificar_trabajador.html', {'form': form})