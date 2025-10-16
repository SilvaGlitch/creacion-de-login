# diagnostico/views.py
from django.shortcuts import render, redirect

diagnosticos = []

def asignar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    return render(request, 'diagnostico/asignar.html')


def evaluar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    mensaje = ''
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo = request.POST.get('equipo')
        diagnostico_text = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo = 'Preventiva' if 'mantenimiento' in solucion.lower() else 'Correctiva'

        nuevo = {
            'estudiante': estudiante,
            'equipo': equipo,
            'diagnostico': diagnostico_text,
            'solucion': solucion,
            'tipo': tipo
        }

        diagnosticos.append(nuevo)
        mensaje = 'Diagnóstico registrado correctamente.'

    return render(request, 'diagnostico/evaluar.html', {'mensaje': mensaje})


def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')

    return render(request, 'diagnostico/listado.html', {'diagnosticos': diagnosticos})

