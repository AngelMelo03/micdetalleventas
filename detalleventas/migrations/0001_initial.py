# Generated by Django 3.2.8 on 2021-11-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalleventas',
            fields=[
                ('codigo_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_producto', models.IntegerField()),
                ('cedula_cliente', models.IntegerField()),
                ('iva_compra', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
            ],
        ),
    ]
