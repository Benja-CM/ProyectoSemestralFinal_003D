from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol      = models.AutoField(primary_key=True, verbose_name='ID de Rol')
    rol_nom     = models.CharField(blank=False, verbose_name='Nombre de Rol')

class Usuario(models.Model):
    id_usuario  = models.AutoField(primary_key=True, verbose_name='ID de Usuario')
    us_rut      = models.CharField(blank=False, verbose_name='Rut de Usuario')
    us_nombre   = models.CharField(blank=False, verbose_name='Nombre de Usuario')
    us_apellido = models.CharField(blank=False, verbose_name='Apellido de Usuario')
    us_telefono = models.CharField(blank=False, verbose_name='Telefono de Usuario')
    rol         = models.ForeignKey(Rol, on_delete=models.CASCADE)
    us_correo   = models.CharField(blank=False, verbose_name='Correo de Usuario')
    us_clave    = models.CharField(blank=False, verbose_name='Clave de Usuario')

class Categoria(models.Model):
    id_cat      = models.AutoField(primary_key=True, verbose_name='ID de Categoria')
    cat_nom     = models.CharField(blank=False, verbose_name='Nombre de Categoria')

class Producto(models.Model):
    id_prod     = models.AutoField(primary_key=True, verbose_name='ID de Producto')
    prod_nom    = models.CharField(blank=False, verbose_name='Nombre de Producto')
    prod_descripción = models.TextField(blank=False)
    prod_precio = models.IntegerField(null=False, blank=False)
    prod_stock  = models.IntegerField(null=False, blank=False)
    prod_imagen = models.ImageField(upload_to="Productos")
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Region(models.Model):
    id_region   = models.AutoField(primary_key=True, verbose_name='ID de Region')
    reg_nom     = models.CharField(blank=False, verbose_name='Nombre de Region')

class Comuna(models.Model):
    id_region   = models.AutoField(primary_key=True, verbose_name='ID de Comuna')
    com_nom     = models.CharField(blank=False, verbose_name='Nombre de Comuna')
    com_cost_envio = models.IntegerField(null=False, blank=False) #Pertenece a la tabla como supertipo
    region      = models.ForeignKey(Region, on_delete=models.CASCADE)

class direccion(models.Model):
    id_dir      = models.AutoField(primary_key=True, verbose_name='ID de Dirección')
    dir_calle   = models.CharField(blank=False, verbose_name='Nombre de Calle')
    dir_numero  = models.IntegerField(null=False, blank=False)
    dir_cod_postal = models.IntegerField(null=False, blank=False)
    usuario      = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comuna      = models.ForeignKey(Comuna, on_delete=models.CASCADE)

class Estado(models.Model):
    id_estado   = models.AutoField(primary_key=True, verbose_name='ID de Estado')
    est_nombre  = models.CharField(blank=False, verbose_name='Nombre de Estado')

class Compra(models.Model):
    id_compra   = models.AutoField(primary_key=True, verbose_name='ID de Compra')
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cop_fechcom = models.DateField(null=False, blank=False)
    cop_fech_desp = models.DateField(null=False, blank=False)
    cop_fech_entr = models.DateField(null=False, blank=False)
    estado      = models.ForeignKey(Estado, on_delete=models.CASCADE)
    com_cost_envio = models.IntegerField(null=False, blank=False) #Debe venir de la tabla Comuna
    cop_total   = models.IntegerField(null=False, blank=False)
    cop_carrito = models.BooleanField(null=False, blank=False)

class Detalle(models.Model):
    id_detalle  = models.AutoField(primary_key=True, verbose_name='ID de Compra')
    compra      = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto    = models.ForeignKey(Producto, on_delete=models.CASCADE)
    de_cantidad = models.IntegerField(null=False, blank=False)
    de_subtotal = models.IntegerField(null=False, blank=False)