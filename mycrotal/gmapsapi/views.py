# views.py
import googlemaps
from django.shortcuts import render
from django.conf import settings

def mostrar_mapa(request):
    context = {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
    }
    return render(request, 'mostrarMapa.html', context)
    #return render(request, 'gmapsapi/mostrarMapa.html', {'api_key': settings.GOOGLE_API_KEY})

def calcular_ruta(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    directions_result = gmaps.directions('Paradero A', 'Paradero B', mode="transit")
    return render(request, 'gmapsapi/calculadora_rutas.html', {'directions_result': directions_result})
