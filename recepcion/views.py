# recepcion/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Lista simulada de equipos recibidos
equipos = []

# Proteger vistas si no está autenticado
def verificar_sesion(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    mensaje = ''
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        equipo = request.POST.get('equipo')
        problema = request.POST.get('problema')

        nuevo_equipo = {
            'cliente': cliente,
            'equipo': equipo,
            'problema': problema
        }

        equipos.append(nuevo_equipo)
        mensaje = 'Equipo registrado con éxito.'

    return render(request, 'recepcion/registrar.html', {'mensaje': mensaje})


def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')
    return render(request, 'recepcion/listado.html', {'equipos': equipos})


def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    equipo_detalle = None
    for equipo in equipos:
        if equipo['cliente'] == nombre:
            equipo_detalle = equipo
            break

    if not equipo_detalle:
        return HttpResponse("Equipo no encontrado")

    return render(request, 'recepcion/detalle.html', {'equipo': equipo_detalle})

