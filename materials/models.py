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
    fecha_ingreso=models.CharField(max_length=16)
    fecha_vencimiento=models.CharField(max_length=10)
    cantidad=models.FloatField()
    ni = models.IntegerField(null=True)
    codigo = models.IntegerField()
    nombre=models.CharField(max_length=50)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    numero= models.CharField(max_length=50)
    codigo_materia = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE) #FOREIGN KEY DE CATEGORIA 
    def str(self):
        return self.nombre