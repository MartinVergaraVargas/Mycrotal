from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import Lector


urlpatterns = [

    path('', Lector.as_view(), name='lector_view'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
