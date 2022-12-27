from django.db import models
# Create your models here.

class Materia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    existencia = models.FloatField(default=0)
    descripcion=models.CharField(max_length=100, null=True)
    def str(self):
        return self.nombre

class Entradas(models.Model):
    ni = models.AutoField(primary_key=True, default=1000)
    fecha_ingreso=models.CharField(max_length=16)
    fecha_vencimiento=models.CharField(max_length=10)
    cantidad=models.FloatField()
    codigo = models.IntegerField()
    nombre=models.CharField(max_length=50)
    oc=models.IntegerField()
    nlote=models.IntegerField()
    proveedor = models.CharField(max_length=50)