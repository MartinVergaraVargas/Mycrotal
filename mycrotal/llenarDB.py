import os
import psycopg2
from django.conf import settings

# Configura la configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mycrotal.settings")
settings.configure()
import django
django.setup()

from gmapsapi.models import Linea  # Asegúrate de importar tu modelo
from gmapsapi.models import Paradero

# Conecta a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="mycrotal",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)

# Crea un cursor
cursor = conn.cursor()

def ingresar_lineas():
    num_lineas = int(input("¿Cuántas líneas deseas ingresar? "))
    for _ in range(num_lineas):
        nombre_linea = input("Nombre de la línea: ")
        new_linea = Linea(nombre=nombre_linea)
        new_linea.save()

def ingresar_paraderos():
    num_paraderos = int(input("¿Cuántos paraderos deseas ingresar? "))
    for _ in range(num_paraderos):
        nombre_paradero = input("Nombre del paradero: ")
        ubicacion_paradero = input("Ubicación del paradero: ")
        new_paradero = Paradero(nombre=nombre_paradero)
        new_paradero.save()

if __name__ == '__main__':
    ingresar_lineas()
    ingresar_paraderos()

# Cierra la conexión
cursor.close()
conn.close()
