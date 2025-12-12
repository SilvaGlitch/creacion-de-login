from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        if usuario == 'inacap' and clave == 'clinica2025':
            request.session['autenticado'] = True
            return redirect('/inicio/')  

        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            request.session['autenticado'] = True
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/inicio/') 
        else:
            messages.error(request, 'Usuario o clave incorrectos.')

    return render(request, 'login/login.html')


def logout_view(request):
    if 'autenticado' in request.session:
        del request.session['autenticado']
    logout(request)
    return redirect('/')  


def inicio(request):
    if not request.session.get('autenticado'):
        return redirect('/')  

    return render(request, 'login/inicio.html')

# En login/views.py, agrega esta función:

def demo_api(request):
    """Página de demostración de la API REST"""
    return render(request, 'login/demo_api.html')