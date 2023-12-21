from django.urls import path
from .views import mostrar_mapa, mostrar_paraderos

urlpatterns = [
    # Otras rutas...
    path('mostrar_mapa/', mostrar_mapa, name='mostrar_mapa'),
    path('mostrar-mapa/<int:paradero_id>/', mostrar_mapa, name='mostrar-mapa'),
    path('mostrar_paraderos/', mostrar_paraderos, name='mostrar_paraderos'),


]

"""
{% for paradero in paraderos %}
    <a href="{% url 'mostrar_mapa_paradero' paradero.id %}">{{ paradero.nombre }}</a>
{% endfor %}
"""