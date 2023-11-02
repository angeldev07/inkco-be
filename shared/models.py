from django.contrib.gis.db import models


class RutaPunto(models.Model):

    nombre = models.CharField()
    geometria = models.DecimalField()

    class Meta:
        db_table = 't_ruta_punto'

class Ruta(models.Model):
    nombre = models.CharField()
    geometria = models.GeometryField()

    class Meta:
        db_table = 't_ruta'

class Evento(models.Model):
    
    nombre = models.CharField()

    class Meta:
        db_table = 't_evento'

class Track(models.Model):
    
    velocidad = models.DecimalField()
    curso = models.DecimalField()
    fecha = models.DateField()  
    geometria = models.GeometryField()
    toponimia = models.CharField()

    class Meta: 
        db_table = 't_track'

class Conductor(models.Model):

    nombre = models.CharField()

    class Meta:
        db_table = 't_conductor'

class Vehiculo(models.Model):

    interno = models.CharField()
    etiqueta = models.CharField()

    class Meta:
        db_table = 't_vehiculo'
