from django.db import models

class Linea(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Micro(models.Model):
    patente = models.CharField(max_length=20, null=True, blank=True)
    idhumano = models.CharField(max_length=10, unique=True)  # Unique para asegurar identificadores únicos
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE, related_name='buses', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Si el objeto aún no tiene un idhumano asignado, genera uno basado en la línea y el número
        if not self.idhumano:
            # Suponiendo que la relación buses se llama 'buses' en el modelo Linea
            total_buses = self.lineas.first().buses.count() + 1 if self.lineas.first() else 1
            self.idhumano = f"{self.lineas.first().nombre}{total_buses}"
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Micro {self.idhumano}'


class Paradero(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)

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