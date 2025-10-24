from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipo 

def verificar_sesion(request):
    if not request.session.get('autenticado') and not request.user.is_authenticated:
        return redirect('/login/')
    return True  

def registrar_equipo(request):
    sesion_valida = verificar_sesion(request)
    if sesion_valida:
        return sesion_valida 

    mensaje = ''
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        contacto = request.POST.get('contacto')
        descripcion_falla = request.POST.get('descripcion_falla')
        estado = request.POST.get('estado')  # si agregaste el campo

        Equipo.objects.create(
            cliente=cliente,
            contacto=contacto,
            descripcion_falla=descripcion_falla,
            estado=estado
        )

        mensaje = 'Equipo registrado con éxito.'

        # Esto debe estar dentro de la función
        return redirect('/recepcion/listado/')  # O usar reverse('listado_equipos')

    return render(request, 'recepcion/registrar.html', {'mensaje': mensaje})


def listado_equipos(request):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida

    equipos = Equipo.objects.all()  
    return render(request, 'recepcion/listado.html', {'equipos': equipos})

def detalle_equipo(request, nombre):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida

    try:
        equipo_detalle = Equipo.objects.get(cliente=nombre)
    except Equipo.DoesNotExist:
        return HttpResponse("Equipo no encontrado")

    return render(request, 'recepcion/detalle.html', {'equipo': equipo_detalle})
