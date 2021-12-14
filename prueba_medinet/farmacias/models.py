from django.db import models

# Create your models here.
class Farmacia(models.Model):
    """
        Farmacia Model

    """

    fecha = models.DateField("Date")

    local_id = models.IntegerField()

    local_nombre = models.CharField("Local Nombre",max_length=400)

    comuna_nombre = models.CharField("Local Nombre",max_length=400)

    fk_localidad = models.IntegerField()

    localidad_nombre = models.CharField("Localidad Nombre",max_length=400)

    local_direccion = models.CharField("Local Direccion",max_length=400)

    funcionamiento_hora_apertura = models.TimeField()

    funcionamiento_hora_cierre = models.TimeField("")

    local_telefono = models.CharField("Local Telefono",max_length=20)

    #Se debería guardar como decimal , no es necesario para este ejercicio práctico
    local_lat = models.CharField("Local Latitud",max_length=100)

    #Se debería guardar como decimal , no es necesario para este ejercicio práctico
    local_lng = models.CharField("Local Longitud",max_length=100)

    funcionamiento_dia = models.CharField("Local Nombre",max_length=50)

    fk_region = models.IntegerField()

    fk_comuna = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        txt = "ID {0} Nombre {1}"
        return txt.format(self.local_id,self.local_nombre)
