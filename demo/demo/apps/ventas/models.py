from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre    = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=50)
    status    = models.BooleanField(default=True)
    def __unicode__(self):
        nombreCompleto = "%s %s- cambiado 5.21pm"%(self.nombre,self.apellidos)
        return nombreCompleto

class producto(models.Model):
    nombre  = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)
    status = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre


