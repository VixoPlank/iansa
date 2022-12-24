from django.db import models

# Create your models here.
class Receta(models.Model):
    id_receta=models.AutoField(primary_key=True)
    producto=models.CharField(max_length=50)

    componente_1=models.CharField(max_length=50)
    codigo_1=models.IntegerField()
    kg_1=models.FloatField()

    componente_2=models.CharField(max_length=50)
    codigo_2=models.IntegerField()
    kg_2=models.FloatField()

    componente_3=models.CharField(max_length=50, null=True)
    codigo_3=models.IntegerField(null=True)
    kg_3=models.FloatField(null=True)

    componente_4=models.CharField(max_length=50,null=True)
    codigo_4=models.IntegerField(null=True)
    kg_4=models.FloatField(null=True)

    componente_5=models.CharField(max_length=50,null=True)
    codigo_5=models.IntegerField(null=True)
    kg_5=models.FloatField(null=True)

    componente_6=models.CharField(max_length=50,null=True)
    codigo_6=models.IntegerField(null=True)
    kg_6=models.FloatField(null=True)

    componente_7=models.CharField(max_length=50,null=True)
    codigo_7=models.IntegerField(null=True)
    kg_7=models.FloatField(null=True)

    componente_8=models.CharField(max_length=50,null=True)
    codigo_8=models.IntegerField(null=True)
    kg_8=models.FloatField(null=True)

    componente_9=models.CharField(max_length=50,null=True)
    codigo_9=models.IntegerField(null=True)
    kg_9=models.FloatField(null=True)

    componente_10=models.CharField(max_length=50,null=True)
    codigo_10=models.IntegerField(null=True)
    kg_10=models.FloatField(null=True)
