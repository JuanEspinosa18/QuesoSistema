# Generated by Django 5.0.2 on 2024-08-28 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_remove_facturacompra_detalles_compra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompradetalle',
            name='factura_compra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalles_compra', to='sales.facturacompra'),
        ),
    ]