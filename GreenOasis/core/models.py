from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol      = models.AutoField(primary_key=True, verbose_name='ID de Rol')
    rol_nom     = models.CharField(max_length=20, blank=False, verbose_name='Nombre de Rol')
    def __str__(self) -> str:
        return self.rol_nom
       
class Usuario(models.Model):
    id_usuario  = models.AutoField(primary_key=True, verbose_name='ID de Usuario')
    us_rut      = models.CharField(max_length=12, blank=True, null=True, verbose_name='Rut de Usuario')
    us_nombre   = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nombre de Usuario')
    us_apellido = models.CharField(max_length=20, blank=True, null=True, verbose_name='Apellido de Usuario')
    us_telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefono de Usuario')
    c_alias     = models.CharField(max_length=25, blank=False, verbose_name='Nombre del Alias')
    c_correo    = models.CharField(max_length=25, blank=False, verbose_name='Correo para Credencial')
    c_password  = models.CharField(max_length=21, blank=False, verbose_name='Clave para Crendencial')
    rol         = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.c_correo

class Categoria(models.Model):
    id_cat      = models.AutoField(primary_key=True, verbose_name='ID de Categoria')
    cat_nom     = models.CharField(max_length=20, blank=False, verbose_name='Nombre de Categoria')
    def __str__(self) -> str:
        return self.cat_nom

class Producto(models.Model):
    id_prod     = models.AutoField(primary_key=True, verbose_name='ID de Producto')
    prod_nom    = models.CharField(max_length=120, blank=False, verbose_name='Nombre de Producto')
    prod_descripcion = models.TextField(blank=False)
    prod_precio = models.IntegerField(null=False, blank=False)
    prod_stock  = models.IntegerField(null=False, blank=False)
    prod_imagen = models.ImageField(upload_to="Productos")
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.prod_nom

# NO MODIFICAR ARRIBA POR DIOS SANTO
# QUE SÍ QUE SÍ

class Region(models.Model):
    id_region   = models.AutoField(primary_key=True, verbose_name='ID de Region')
    reg_nom     = models.CharField(max_length=50, blank=False, verbose_name='Nombre de Region')
    def __str__(self) -> str:
        return self.reg_nom

class Comuna(models.Model):
    id_com   = models.AutoField(primary_key=True, verbose_name='ID de Comuna')
    com_nom     = models.CharField(max_length=50, blank=False, verbose_name='Nombre de Comuna')
    com_cost_envio = models.IntegerField(null=False, blank=False) #Debe venir de la otra tabla
    region      = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.com_nom

class Direccion(models.Model):
    id_dir      = models.AutoField(primary_key=True, verbose_name='ID de Dirección')
    dir_calle   = models.CharField(max_length=50, blank=False, verbose_name='Nombre de Calle')
    dir_numero  = models.IntegerField(null=False, blank=False)
    dir_cod_postal = models.IntegerField(null=False, blank=False)
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comuna      = models.ForeignKey(Comuna, on_delete=models.CASCADE)

# NO SE COMO HACERLO

class Compra(models.Model):
    id_compra   = models.AutoField(primary_key=True, verbose_name='ID de Compra')
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cop_fechcom = models.DateField()
    cop_fech_entr  = models.DateField()
    com_cost_envio = models.IntegerField() #Debe venir de la tabla Comuna
    cop_total   = models.IntegerField()
    
class Detalle(models.Model):
    id_detalle  = models.AutoField(primary_key=True, verbose_name='ID de Detalle')
    compra     = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto    = models.ForeignKey(Producto, on_delete=models.CASCADE)
    de_cantidad = models.IntegerField(null=False, blank=False)
    de_subtotal = models.IntegerField(null=False, blank=False)