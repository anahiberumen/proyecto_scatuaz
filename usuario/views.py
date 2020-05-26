from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UsuarioForm, CambiarContrasenaForm, ModificarUsuarioForm
from .models import UserSCATUAZ
from django.contrib.auth import login, authenticate

# Create your views here.


@login_required
def lista_usuario(request):
    if request.user.is_superuser:
        usuarios = UserSCATUAZ.objects.all()
        context = {
            'actual': 'usuario',
            'usuarios': usuarios,
        }
        return render(request, 'lista_usuario.html', context)
    return redirect('lista_trabajador')


@login_required
def agregar_usuario(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_usuario')
        else:
            form = UsuarioForm()
        return render(request, 'agregar_usuario.html', {'form': form})
    return redirect('lista_trabajador')
    


@login_required
def eliminar_usuario(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            usuario = UserSCATUAZ.objects.get(pk=id)
            usuario.delete()
            return redirect('lista_usuario')
        else:
            usuario = UserSCATUAZ.objects.get(pk=id)
            return render(request, 'confirm_delete_user.html', {'usuario': usuario})
    return redirect('lista_trabajador')
        


@login_required
def modificar_usuario(request, id):
    if request.user.is_superuser:
        usuario = UserSCATUAZ.objects.get(pk=id)
        if request.method == 'POST':
            form = ModificarUsuarioForm(request.POST, instance=usuario)
            print(form)
            if form.is_valid():
                print('es valido')
                form.save()
                return redirect('lista_usuario')
            else:
                print('no es valido')
        else:
            form = ModificarUsuarioForm(instance=usuario)
        return render(request, 'modificar_usuario.html', {'form': form, 'usuario': usuario, 'nombre': usuario.__str__})
    return redirect('lista_trabajador')



@login_required
def cambiar_contrasena(request, id):
    if request.user.is_superuser:
        usuario = UserSCATUAZ.objects.get(pk=id)
        if request.method == 'POST':
            form = CambiarContrasenaForm(usuario, data=request.POST)
            if form.is_valid():
                form.clean_new_password2()
                form.save()
                return redirect('lista_usuario')
        else:
            form = CambiarContrasenaForm(usuario)
        return render(request, 'cambiar_contrasena.html', {'form': form, 'usuario': usuario})
    return redirect('lista_trabajador')
    

@login_required
def ver_usuario(request, id):
    if request.user.is_superuser:
        usuario = UserSCATUAZ.objects.get(pk=id)
        context = {
            'usuario': usuario,
        }
        return render(request, 'ver_usuario.html', context)
    return redirect('lista_trabajador')
    