from django.db import models


# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=200, unique=True, null=False)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return {
            f"Museo {self.nombre} de la Ciudad {self.ciudad} fundada en {self.anio_fundacion}"
        }


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")

    def __str__(self):
        return {
            f"Guia {self.nombre_completo} con experiencia de {self.anios_experiencia_guia} que habla {self.idiomas_hablados}"
        }


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=200)

    museo = models.ForeignKey(
        Museo, on_delete=models.CASCADE, related_name="exhibiciones"
    )

    def __str__(self):
        return {
            f"La exhibicion {self.titulo_exhibicion} con duracion de {self.duracion_meses} que costo {self.costo_produccion} con la tematica {self.tematica}"
        }
