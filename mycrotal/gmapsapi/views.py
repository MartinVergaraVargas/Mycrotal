# views.py
import googlemaps
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from datosMicros.models import Paradero
from django.core.serializers import serialize
from django.http import JsonResponse

"""def mostrar_mapa(request):
    paraderos = serialize('json', Paradero.objects.all(), fields=('nombre', 'ubicacion'))
    context = {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
        'paraderos': paraderos,
    }
    return render(request, 'mostrarMapa.html', context)
"""
def mostrar_paraderos(request):
    paraderos = Paradero.objects.all()
    context = {'paraderos': paraderos}
    return render(request, 'mostrar_paraderos.html', context)


def mostrar_mapa(request, paradero_id=None):
    talca_coordinates = {'lat': -35.4261, 'lng': -71.6485}
    if paradero_id:
        paradero = get_object_or_404(Paradero, id=paradero_id)
        latitud, longitud = map(float, paradero.ubicacion.split(', '))
        context = {
            'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
            'paradero': {
                'nombre': paradero.nombre,
                'ubicacion': {'lat': latitud, 'lng': longitud}
            },
        }
    else:
        context = {
            'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
            'talca_coordinates': talca_coordinates,
        }

    return render(request, 'mostrarMapa.html', context)
#####################################################################################################
def calcular_ruta(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    directions_result = gmaps.directions('Paradero A', 'Paradero B', mode="transit")
    return render(request, 'gmapsapi/calculadora_rutas.html', {'directions_result': directions_result})