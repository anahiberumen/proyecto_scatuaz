from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('lista_trabajador')
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                usuario = authenticate(
                    request,
                    username=username,
                    password=password
                )

                if usuario is not None:
                    login(request, usuario)
                    return redirect('lista_trabajador')

        return render(request, 'login/iniciar.html', {'form': form})


def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('iniciar_sesion')
