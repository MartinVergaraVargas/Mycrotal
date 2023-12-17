from django.urls import path
from .views import mostrar_mapa

urlpatterns = [
    # Otras rutas...
    path('mostrar-mapa/', mostrar_mapa, name='mostrar_mapa'),
]