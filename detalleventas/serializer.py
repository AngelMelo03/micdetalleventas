from rest_framework import serializers
from .models import *

class DetalleventasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detalleventas
        fields = ['codigo_venta', 'codigo_producto', 'cedula_cliente', 'consecutivo','iva_compra', 'precio_compra', 'precio_venta']
