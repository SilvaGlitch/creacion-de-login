from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        if usuario == 'inacap' and clave == 'clinica2025':
            request.session['autenticado'] = True
            return redirect('/recepcion/registrar/')

        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/recepcion/')
        else:
            messages.error(request, 'Usuario o clave incorrectos.')

    return render(request, 'login/login.html')


def logout_view(request):

    if 'autenticado' in request.session:
        del request.session['autenticado']
    logout(request)
    return redirect('/')
