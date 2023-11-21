from django.db import models

class Linea(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Paradero(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField()
    paradero = models.ForeignKey(Paradero, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ruta de {self.linea.nombre}'

"""
ruta = Ruta(linea=linea_instancia, orden=1, paradero=paradero_instancia)
ruta.save()
"""