# Generated by Django 4.2.1 on 2023-06-24 00:43

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
                ('cop_fechcom', models.DateField(blank=True, null=True)),
                ('cop_fech_entr', models.DateField(blank=True, null=True)),
                ('com_cost_envio', models.IntegerField(blank=True, null=True)),
                ('cop_total', models.IntegerField(blank=True, null=True)),
                ('cop_realizada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_com', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Comuna')),
                ('com_nom', models.CharField(max_length=50, verbose_name='Nombre de Comuna')),
                ('com_cost_envio', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la pregunta')),
                ('pregunta_pred', models.CharField(max_length=100, verbose_name='Pregunta')),
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
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Usuario')),
                ('us_rut', models.CharField(blank=True, max_length=12, null=True, verbose_name='Rut de Usuario')),
                ('us_nombre', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre de Usuario')),
                ('us_apellido', models.CharField(blank=True, max_length=20, null=True, verbose_name='Apellido de Usuario')),
                ('us_telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono de Usuario')),
                ('c_alias', models.CharField(max_length=25, verbose_name='Nombre del Alias')),
                ('c_correo', models.CharField(max_length=25, verbose_name='Correo para Credencial')),
                ('c_password', models.CharField(max_length=21, verbose_name='Clave para Crendencial')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Respuesta')),
                ('respuesta', models.CharField(max_length=100, verbose_name='Respuesta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pregunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Producto')),
                ('prod_nom', models.CharField(max_length=120, verbose_name='Nombre de Producto')),
                ('prod_descripcion', models.TextField()),
                ('prod_precio', models.IntegerField()),
                ('prod_stock', models.IntegerField()),
                ('prod_imagen', models.ImageField(upload_to='Productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Historial')),
                ('nom_prod', models.CharField(max_length=50, verbose_name='Nombre de Producto')),
                ('img_prod', models.ImageField(upload_to='', verbose_name='Foto de Producto')),
                ('cant_prod', models.IntegerField(verbose_name='Foto de Producto')),
                ('precio_prod', models.IntegerField(verbose_name='Precio del producto')),
                ('subtotal_prod', models.IntegerField(verbose_name='Subtotal')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_dir', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Dirección')),
                ('dir_calle', models.CharField(blank=True, max_length=50, verbose_name='Nombre de Calle')),
                ('dir_numero', models.IntegerField(blank=True, null=True)),
                ('dir_cod_postal', models.IntegerField(blank=True, null=True)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Detalle')),
                ('de_cantidad', models.IntegerField()),
                ('de_subtotal', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.direccion'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
