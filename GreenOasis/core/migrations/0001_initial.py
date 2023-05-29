# Generated by Django 4.2.1 on 2023-05-29 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_cat', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Categoria')),
                ('cat_nom', models.CharField(max_length=20, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Compra')),
                ('cop_fechcom', models.DateField()),
                ('cop_fech_desp', models.DateField()),
                ('cop_fech_entr', models.DateField()),
                ('com_cost_envio', models.IntegerField()),
                ('cop_total', models.IntegerField()),
                ('cop_carrito', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Comuna')),
                ('com_nom', models.CharField(max_length=25, verbose_name='Nombre de Comuna')),
                ('com_cost_envio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Credencial',
            fields=[
                ('id_credencial', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Crendencial')),
                ('c_alias', models.CharField(max_length=25, verbose_name='Nombre del Alias')),
                ('c_correo', models.CharField(max_length=25, verbose_name='Correo para Credencial')),
                ('c_password', models.CharField(max_length=21, verbose_name='Clave para Crendencial')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Estado')),
                ('est_nombre', models.CharField(max_length=20, verbose_name='Nombre de Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Region')),
                ('reg_nom', models.CharField(max_length=25, verbose_name='Nombre de Region')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Rol')),
                ('rol_nom', models.CharField(max_length=20, verbose_name='Nombre de Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id_tarjeta', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Tarjeta')),
                ('t_numero', models.CharField(max_length=20, verbose_name='Numero de Tarjeta')),
                ('t_fvenc', models.CharField(max_length=20, verbose_name='Fecha de Vencimiento de Tarjeta')),
                ('t_cvv', models.IntegerField(verbose_name='Codigo de Verificación de Tarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Usuario')),
                ('us_rut', models.CharField(max_length=12, verbose_name='Rut de Usuario')),
                ('us_nombre', models.CharField(max_length=20, verbose_name='Nombre de Usuario')),
                ('us_apellido', models.CharField(max_length=20, verbose_name='Apellido de Usuario')),
                ('us_telefono', models.CharField(max_length=15, verbose_name='Telefono de Usuario')),
                ('credencial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.credencial')),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Producto')),
                ('prod_nom', models.CharField(max_length=20, verbose_name='Nombre de Producto')),
                ('prod_descripcion', models.TextField()),
                ('prod_precio', models.IntegerField()),
                ('prod_stock', models.IntegerField()),
                ('prod_imagen', models.ImageField(upload_to='Productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_dir', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Dirección')),
                ('dir_calle', models.CharField(max_length=25, verbose_name='Nombre de Calle')),
                ('dir_numero', models.IntegerField()),
                ('dir_cod_postal', models.IntegerField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Compra')),
                ('de_cantidad', models.IntegerField()),
                ('de_subtotal', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.AddField(
            model_name='credencial',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
        migrations.AddField(
            model_name='compra',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
