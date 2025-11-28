# entrega/views.py
from django.shortcuts import render, redirect
from recepcion.models import Equipo  # Importar el modelo real

# Lista para almacenar entregas temporalmente (en una app real usarías un modelo)
entregas = []

def verificar_cliente(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    cliente_info = None
    mensaje = ''

    if request.method == 'POST':
        nombre_cliente = request.POST.get('cliente', '').strip()
        
        if nombre_cliente:
            try:
                # BUSCAR EN LA BASE DE DATOS REAL
                equipo = Equipo.objects.get(cliente__iexact=nombre_cliente)
                
                cliente_info = {
                    'cliente': equipo.cliente,
                    'equipo': f"{getattr(equipo, 'tipo_equipo', 'Equipo')} - {equipo.descripcion_falla[:30]}...",
                    'diagnostico': equipo.descripcion_falla,
                    'solucion': 'Diagnóstico pendiente',  # Por defecto
                    'tipo': 'Por determinar',
                    'estado_actual': getattr(equipo, 'estado', 'En proceso')
                }
                
            except Equipo.DoesNotExist:
                # Si no encuentra exacto, buscar parcialmente
                equipos = Equipo.objects.filter(cliente__icontains=nombre_cliente)
                if equipos.exists():
                    equipo = equipos.first()
                    cliente_info = {
                        'cliente': equipo.cliente,
                        'equipo': f"{getattr(equipo, 'tipo_equipo', 'Equipo')}",
                        'diagnostico': equipo.descripcion_falla,
                        'solucion': 'Diagnóstico pendiente',
                        'tipo': 'Por determinar',
                        'estado_actual': getattr(equipo, 'estado', 'En proceso')
                    }
                else:
                    mensaje = f'No se encontró ningún equipo para el cliente: {nombre_cliente}'
                    
            except Exception as e:
                mensaje = f'Error al buscar cliente: {str(e)}'

    return render(request, 'entrega/verificar.html', {
        'cliente': cliente_info,
        'mensaje': mensaje
    })

def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones', '')

        entrega = {
            'cliente': cliente,
            'estado': estado,
            'observaciones': observaciones
        }

        entregas.append(entrega)
        request.session['comprobante_cliente'] = cliente

        return redirect('/entrega/comprobante/')

    return redirect('/entrega/verificar/')

def comprobante_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    cliente = request.session.get('comprobante_cliente')
    
    if not cliente:
        return render(request, 'entrega/comprobante.html', {'error': 'No se encontró información del cliente.'})

    # Buscar la entrega más reciente para este cliente
    entrega_final = None
    for e in reversed(entregas):  # Buscar desde la más reciente
        if e['cliente'] == cliente:
            entrega_final = e
            break

    if not entrega_final:
        return render(request, 'entrega/comprobante.html', {'error': 'No se encontró información de entrega.'})

    return render(request, 'entrega/comprobante.html', {
        'cliente': cliente,
        'entrega': entrega_final
    })
    