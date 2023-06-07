# Generated by Django 4.2.1 on 2023-06-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_comuna_region_delete_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='dir_calle',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre de Calle'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='dir_cod_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='dir_numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
