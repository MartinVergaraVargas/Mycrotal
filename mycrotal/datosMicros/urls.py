from django.urls import path
from .views import *

urlpatterns = [
    #path("", HomeView.as_view(), name='my_home_view'), 
    path("mapa", MapView.as_view(), name='mapa')
   

]