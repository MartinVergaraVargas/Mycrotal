import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mycrotal.settings")
django.setup()

from datosMicros.models import Linea, Paradero, Ruta

# Carga de datos
linea1 = Linea.objects.create(nombre='Linea 1')
paradero1 = Paradero.objects.create(nombre='Paradero A', ubicacion='Ubicacion A')
paradero2 = Paradero.objects.create(nombre='Paradero B', ubicacion='Ubicacion B')

ruta1 = Ruta.objects.create(linea=linea1, orden=1, paradero=paradero1)
ruta2 = Ruta.objects.create(linea=linea1, orden=2, paradero=paradero2)
