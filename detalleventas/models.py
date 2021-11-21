from django.db import models

# Create your models here.
class Detalleventas(models.Model):
    codigo_venta=models.IntegerField(primary_key=True)
    codigo_producto=models.IntegerField()
    cedula_cliente=models.IntegerField()
    consecutivo=models.IntegerField()
    iva_compra=models.FloatField()
    precio_compra=models.FloatField()
    precio_venta=models.FloatField()
