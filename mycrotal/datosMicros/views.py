from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect
from .models import *
import googlemaps
from django.conf import settings
from .forms import *
from datetime import datetime

from django.shortcuts import render, redirect
from .models import Linea, Paradero


# Create your views here.

def listar_lineas_paraderos(request):
    lineas = Linea.objects.all()
    paraderos = Paradero.objects.all()

    if request.method == "POST":
        # Procesar el formulario para agregar nuevos datos
        # Esto dependerá de cómo estés manejando el formulario en Django
        # Por ejemplo:
        nombre = request.POST.get('nombre')
        numero = request.POST.get('numero')
        # Crear un nuevo objeto de Linea con los datos y guardarlo en la base de datos

    return render(request, 'gmapsapi/listar_lineas_paraderos.html', {'lineas': lineas, 'paraderos': paraderos})



class MapView(View): 
    template_name = "mapa.html"

    def get(self,request): 
        key = settings.GOOGLE_API_KEY
        eligable_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []

        for a in eligable_locations: 
            data = {
                'lat': float(a.lat), 
                'lng': float(a.lng), 
                'name': a.name
            }

            locations.append(data)


        context = {
            "key":key, 
            "locations": locations
        }

        return render(request, self.template_name, context)
