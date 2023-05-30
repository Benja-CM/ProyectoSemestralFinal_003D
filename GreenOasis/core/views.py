from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from .models import Rol, Usuario, Producto, Direccion, Comuna, Region, Credencial, Tarjeta, Categoria

# Create your views here.
def index(request):
    return render(request, 'core/Index.html')

def ong(request):
    return render(request, 'core/ong.html')

def product(request):
   
    return render(request, 'core/product1.html')

def profile(request):
    return render(request, 'core/profile.html')

def cart(request):
    return render(request, 'core/cart.html')

def search(request):
    return render(request, 'core/search.html')

def conf_pago(request):
    return render(request, 'core/conf_pago.html')

def create_acc(request):
    return render(request, 'core/create_acc.html')

def h_buy(request):
    return render(request, 'core/h_buy.html')

def h_prod1(request):
    return render(request, 'core/h_prod1.html')

def p_acc(request):
    return render(request, 'core/p_acc.html')

def p_info(request):
    return render(request, 'core/p_info.html')

def p_pch(request):
    return render(request, 'core/p_pch.html')

def p_pch(request):
    return render(request, 'core/p_pch.html')

def pss_fg(request):
    return render(request, 'core/pss_fg.html')

def vent_edit(request):
    return render(request, 'core/vent_edit.html')

def vent_editDato(request,id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id_prod = id)
    contexto = {
        "datos": producto,
        "listaCategorias": categorias
    }
    
    return render(request, 'core/vent_edit.html')

def actualizarProducto(request):
    id      = request.POST['ID']
    nombre  = request.POST['nombre']
    descripcion = request.POST['desc']
    precio  = request.POST['precio']
    stock   = request.POST['stock']
    imagen  = request.FILE['imagen']
    categoria   = request.POST['categoria']

    producto = Producto.objest.get(id_prod = id)
    producto.prod_nom = nombre
    producto.prod_descripcion = descripcion
    producto.prod_precio = precio
    producto.prod_stock = stock
    producto.prod_imagen = imagen
    
    registroCategoria = Categoria.objects.get(id_cat = categoria)
    producto.categoria = registroCategoria
    
    producto.save()
    
    return redirect('listado')


def vent_ing(request):
    return render(request, 'core/vent_ing.html')

def vent_list(request):
    productos = Producto.objects.all()

    contexto = {
        "listado": productos
    }
    return render(request, 'core/vent_list.html',contexto)


# INGRESAR DE INFORMACION DEL USUARIO
@transaction.atomic
def registrarInfUS(request):
    rut_u       = request.POST['rut']
    nombre_u    = request.POST['nombre']
    apellido_u  = request.POST['apellido']
    telefono_u  = request.POST['telefono']

    with transaction.atomic():
        registrarCU = Credencial.objects.latest('id_credencial')
        registrarTarjeta = Tarjeta.objects.latest('id_tarjeta')

        Usuario.objects.create(us_rut=rut_u, us_nombre=nombre_u, us_apellido=apellido_u, 
                               us_telefono=telefono_u, tarjeta=registrarTarjeta, credencial=registrarCU)
        
    return redirect('p_info')
    
# INGRESAR INFORMACION DE CUENTA
def registrarInfAC(request):
    alias_u     = request.POST['alias']
    correo_u    = request.POST['email']
    password_u  = request.POST['password']
    rol_u       = 1
    
    role        = Rol.objects.get(id_rol = rol_u)

    Credencial.objects.create(c_alias = alias_u, c_correo = correo_u, c_password = password_u, rol = role)
    
    return redirect('index')

# INGRESAR INFORMACION DE TAJETA
def registrarTarjeta(request):
    tar_numero  = request.POST['n_tarjeta']
    tar1_fvenc  = request.POST['f1_venc']
    tar2_fvenc  = request.POST['f2_venc']
    tar_cvv     = request.POST['cds']
    
    Tarjeta.objects.create(t_numero = tar_numero, t_fvenc = tar1_fvenc + '/' + tar2_fvenc, t_cvv = tar_cvv)
    
    return redirect('p_pch')

# INGRESAR DE PRODUCTOS
def resgistrarProducto(request):
    pr_nom      = request.POST['nombre']
    pr_descripcion = request.POST['desc']
    pr_precio   = request.POST['precio']
    pr_stock    = request.POST['stock']
    pr_imagen   = request.FILES['imagen']
    pr_cat      = request.POST['sa-cat']

    registroCat = Categoria.objects.get(id_cat = pr_cat)

    Producto.objects.create(prod_nom = pr_nom, prod_descripcion = pr_descripcion, prod_precio = pr_precio,
                        prod_stock = pr_stock, prod_imagen = pr_imagen, categoria = registroCat)
    
    return redirect('vent_list')

def eliminarProducto(request,id):
    producto = Producto.objects.get(id_prod = id)
    producto.delete()
    
    return redirect('vent_list')