from django.db import models

class Linea(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.nombre

class Paradero(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)  # Debes considerar el tipo de dato correcto para las coordenadas
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    id_linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
    paraderos = models.ManyToManyField(Paradero, through='ParaderoRuta')

    def __str__(self):
        return f'Ruta de {self.id_linea}'

class ParaderoRuta(models.Model):
    id = models.AutoField(primary_key=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    paradero = models.ForeignKey(Paradero, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField()

    def __str__(self):
        return f'Paradero {self.paradero} en Ruta {self.ruta}'
