from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Equipo 

def verificar_sesion(request):
    if not request.session.get('autenticado') and not request.user.is_authenticated:
        return redirect('/login/')
    return True  

def registrar_equipo(request):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida 

    mensaje = ''
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        contacto = request.POST.get('contacto')
        descripcion_falla = request.POST.get('descripcion_falla')
        estado = request.POST.get('estado', 'recibido')  # Valor por defecto

        # Validación básica
        if cliente and descripcion_falla:
            Equipo.objects.create(
                cliente=cliente,
                contacto=contacto,
                descripcion_falla=descripcion_falla,
                estado=estado
            )
            messages.success(request, 'Equipo registrado con éxito.')
            return redirect('listado_equipos')
        else:
            messages.error(request, 'Cliente y descripción de falla son obligatorios.')

    return render(request, 'recepcion/registrar.html', {'mensaje': mensaje})

def listado_equipos(request):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida

    equipos = Equipo.objects.all().order_by('-id')  # Ordenar por más reciente primero
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

# NUEVA VISTA: Detalle por ID (para compatibilidad con las URLs nuevas)
def detalle_equipo_por_id(request, id):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida

    try:
        equipo_detalle = get_object_or_404(Equipo, id=id)
    except Equipo.DoesNotExist:
        return HttpResponse("Equipo no encontrado")

    return render(request, 'recepcion/detalle.html', {'equipo': equipo_detalle})

# NUEVA VISTA: Editar equipo
def editar_equipo(request, id):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida

    equipo = get_object_or_404(Equipo, id=id)
    
    if request.method == 'POST':
        # Actualizar con los datos del formulario
        equipo.cliente = request.POST.get('cliente', equipo.cliente)
        equipo.contacto = request.POST.get('contacto', equipo.contacto)
        equipo.descripcion_falla = request.POST.get('descripcion_falla', equipo.descripcion_falla)
        equipo.estado = request.POST.get('estado', equipo.estado)
        equipo.save()
        
        messages.success(request, f'Equipo de {equipo.cliente} actualizado exitosamente!')
        return redirect('listado_equipos')
    
    # Pasar el equipo al template para pre-cargar el formulario
    return render(request, 'recepcion/editar.html', {'equipo': equipo})

# NUEVA VISTA: Eliminar equipo
def eliminar_equipo(request, id):
    sesion_valida = verificar_sesion(request)
    if sesion_valida != True:
        return sesion_valida

    equipo = get_object_or_404(Equipo, id=id)
    
    if request.method == 'POST':
        cliente_nombre = equipo.cliente
        equipo.delete()
        messages.success(request, f'Equipo de {cliente_nombre} eliminado exitosamente!')
        return redirect('listado_equipos')
    
    # Mostrar confirmación
    return render(request, 'recepcion/eliminar.html', {'equipo': equipo})
