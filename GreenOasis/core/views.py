from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from .models import Rol, Usuario, Producto, Direccion, Comuna, Region, Categoria, Detalle, Compra

# Create your views here.
def index(request):
    return render(request, 'core/Index.html')

def ong(request):
    return render(request, 'core/ong.html')

def product(request):
    return render(request, 'core/product1.html')

@login_required
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

def vent_ing(request):
    return render(request, 'core/vent_ing.html')

# PERMITE EDITAR UN PRODUCTO SELECCIONADO DE LA LISTA
@login_required
def vent_edit(request, id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id_prod = id)
    contexto = {
        "datos": producto,
        "listaCategorias": categorias
    }
    
    return render(request, 'core/vent_edit.html', contexto)

# LISTA LOS PRODUCTOS DE LA BASE DE DATOS
@login_required
def vent_list(request):
    productos = Producto.objects.all()
    contexto = {
        "listado": productos
    }
    return render(request, 'core/vent_list.html',contexto)

# LISTA LOS PRODUCTOS DE LA BASE DE DATOS
def index(request):
    productos = Producto.objects.all()
    contexto = {
        "listado": productos
    }
    return render(request, 'core/Index.html',contexto)

# FILTRO DE PRODUCTOS EN FUNCION DE CATEGORIA
def search(request, categoria_id):
    if categoria_id == 5:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(categoria=categoria_id)

    contexto = {
        'listado': productos
    }

    return render(request, 'core/search.html', contexto)


# ACTUALIZACION DE LA INFORMACION A LA BASE DE DATOS
def actualizarProducto(request):
    id      = request.POST['ID']
    nombre  = request.POST['nombre']
    descripcion = request.POST['desc']
    precio  = request.POST['precio']
    stock   = request.POST['stock']
    imagen  = request.FILES['imagen']
    categoria   = request.POST['categoria']

    producto = Producto.objects.get(id_prod = id)
    producto.prod_nom = nombre
    producto.prod_descripcion = descripcion
    producto.prod_precio = precio
    producto.prod_stock = stock
    producto.prod_imagen = imagen
    
    registroCategoria = Categoria.objects.get(id_cat = categoria)
    producto.categoria = registroCategoria
    
    messages.add_message(request, messages.SUCCESS, '¡El producto se ha modificado exitosamente!')
    producto.save()
    
    return redirect('vent_list')

# INGRESAR DE INFORMACION DEL USUARIO
@login_required
def registrarInfUS(request):
    rut_u = request.POST['rut']
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    telefono_u = request.POST['telefono']

    # Actualizar el usuario actual
    Usuario.objects.filter(c_alias=request.user.username).update(
        us_rut=rut_u,
        us_nombre=nombre_u,
        us_apellido=apellido_u,
        us_telefono=telefono_u
    )
    return redirect('p_info')
        
    
# INGRESAR INFORMACION DE CUENTA
def registrarInfAC(request):
    alias_u = request.POST['alias']
    correo_u = request.POST['email']
    password_u = request.POST['password']
    rol_u = 1
    role = Rol.objects.get(id_rol=rol_u)

    Usuario.objects.create(c_alias=alias_u, c_correo=correo_u, c_password=password_u, rol=role)
    user = User.objects.create_user(username=alias_u, email=correo_u, password=password_u)
    user.is_active = True
    user.is_staff = False
    user.save()
    return redirect('index')

# INGRESAR DE PRODUCTOS
@login_required
def registrarProducto(request):
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

# ELIMINAR PRODUCTOS DE LA BASE DE DATOS
@login_required
def eliminarProducto(request,id):
    producto = Producto.objects.get(id_prod = id)
    producto.delete()
    
    return redirect('vent_list')

# MUESTRA LA INFORMACION DEL PRODUCTO
def product1(request, id):
    producto = Producto.objects.get(id_prod = id)
    contexto = {
        "p": producto
    }
    
    return render(request, 'core/product1.html', contexto)

# PERMITE INICIAR SESION EN LA PAGINA   
def iniciar_sesion(request):
    print("1")
    user1 = request.POST['email']
    pass1 = request.POST['password']
    try:
        print(f"1- {user1}")
        user = User.objects.get(username = user1)
    except User.DoesNotExist:
        print("3")
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect('index')

    pass_valid = check_password(pass1, user.password)
    print("4")
    if not pass_valid:
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect('index')
    
    user2 = Usuario.objects.get(c_alias=user1, c_password=pass1)
    user = authenticate(request, username=user1, password=pass1)
    
    if user is not None:
        login(request, user)
        print("2")
        if user2.rol.id_rol == 1:
            return redirect('profile')
        # else:    (esto es para cuando la vista de administrador nos falta esa pagina)
        #     contexto = {"usuario": correo2}
        #     return render(request, '.html', contexto)
    else:
        print("8")
    
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def registrarDetalle(request, producto_id, precio):
    usuario = request.user.username
    compra = Compra.objects.filter(usuario = usuario)
    producto = Producto.objects.get(id_prod = producto_id)
    dr_cantidad = request.POST['cantidad']
    dr_subtotal = precio * dr_cantidad
    
    Detalle.objects.create(id_compra = compra.id_compra, producto = producto, de_cantidad = dr_cantidad, de_subtotal = dr_subtotal)
    
    return redirect('search')