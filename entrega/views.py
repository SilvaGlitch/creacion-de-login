from django.shortcuts import render, redirect


entregas = []

diagnosticos_simulados = [
    {
        'cliente': 'Pedro',
        'equipo': 'Notebook HP',
        'diagnostico': 'Placa suelta',
        'solucion': 'Reemplazo de tornillos',
        'tipo': 'Correctiva'
    },
    {
        'cliente': 'Maria',
        'equipo': 'Laptop Dell',
        'diagnostico': 'Pantalla parpadea',
        'solucion': 'Reemplazo de pantalla',
        'tipo': 'Correctiva'
    },
]

def verificar_cliente(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    cliente_info = None
    mensaje = ''

    if request.method == 'POST':
        nombre = request.POST.get('cliente', '').strip()
        if nombre:
            for d in diagnosticos_simulados:
                if d['cliente'].lower() == nombre.lower():
                    cliente_info = d
                    break
            if not cliente_info:
                mensaje = 'Cliente no encontrado.'

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
        observaciones = request.POST.get('observaciones')

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
    datos = None
    entrega_final = None

    for d in diagnosticos_simulados:
        if d['cliente'] == cliente:
            datos = d
            break

    for e in entregas:
        if e['cliente'] == cliente:
            entrega_final = e
            break

    if not datos or not entrega_final:
        return render(request, 'entrega/comprobante.html', {'error': 'No se encontró información.'})

    return render(request, 'entrega/comprobante.html', {
        'diagnostico': datos,
        'entrega': entrega_final
    })
