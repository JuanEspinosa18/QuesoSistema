# Generated by Django 5.0.2 on 2024-09-17 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiaprima',
            name='descontinuado',
            field=models.BooleanField(default=False, verbose_name='Descontinuado'),
        ),
    ]