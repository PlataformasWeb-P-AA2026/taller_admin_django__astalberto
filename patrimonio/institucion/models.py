from django.db import models
from django.db.models import Sum, Max


# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=200, unique=True, null=False)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def costo_total_produccion(self):
        exhibiciones = self.exhibiciones.all()
        suma = 0

        for exhibicion in exhibiciones:
            suma += exhibicion.costo_produccion

        return suma

    def guias_mas_experimentados(self):
        experiencias = list(self.guias.values_list("anios_experiencia_guia", flat=True))
        if not experiencias:
            return ""
        max_exp = max(experiencias)
        nombres = self.guias.filter(anios_experiencia_guia=max_exp).values_list(
            "nombre_completo", flat=True
        )
        return ", ".join(nombres)

    def __str__(self):
        return (
            f"Museo {self.nombre} de la Ciudad de {self.ciudad} fundada en {self.anio_fundacion}"
            f" con el costo total de: {self.costo_total_produccion()}"
            f" y con los guias mas experimentados {self.guias_mas_experimentados()}"
        )


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")

    def __str__(self):
        return (
            f"Guia {self.nombre_completo} con experiencia de {self.anios_experiencia_guia} años"
            f" que habla {self.idiomas_hablados}"
        )


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=200)

    museo = models.ForeignKey(
        Museo, on_delete=models.CASCADE, related_name="exhibiciones"
    )

    def __str__(self):
        return (
            f"La exhibicion {self.titulo_exhibicion} con duracion de {self.duracion_meses} que costo "
            f"{self.costo_produccion} con la tematica de {self.tematica}"
        )
