# views.py
import googlemaps
from django.shortcuts import render
from django.conf import settings
from datosMicros.models import Paradero
from django.core.serializers import serialize
from django.http import JsonResponse


""" def mostrar_mapa(request):
    context = {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
    }
    return render(request, 'mostrarMapa.html', context)
    #return render(request, 'gmapsapi/mostrarMapa.html', {'api_key': settings.GOOGLE_API_KEY})
 """
def mostrar_mapa(request):
    paraderos = serialize('json', Paradero.objects.all(), fields=('nombre', 'ubicacion'))
    context = {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
        'paraderos': paraderos,
    }
    return render(request, 'mostrarMapa.html', context)


def calcular_ruta(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    directions_result = gmaps.directions('Paradero A', 'Paradero B', mode="transit")
    return render(request, 'gmapsapi/calculadora_rutas.html', {'directions_result': directions_result})