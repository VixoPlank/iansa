from django.db import models
# Create your models here.
def field_start_from_1001():
    last_entry = Entradas.objects.all().order_by('ni').last()
    if last_entry:
        return last_entry.ni + 1
    return 1001


class Materia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    existencia = models.FloatField(default=0)
    descripcion=models.CharField(max_length=100)
    def str(self):
        return self.nombre

class Entradas(models.Model):
    ni = models.AutoField(primary_key=True, default=field_start_from_1001)
    fecha_ingreso=models.CharField(max_length=16)
    fecha_vencimiento=models.CharField(max_length=10)
    cantidad=models.FloatField()
    codigo = models.IntegerField()
    nombre=models.CharField(max_length=50)
    oc=models.IntegerField()
    nlote=models.CharField(max_length=30)
    proveedor = models.CharField(max_length=50)