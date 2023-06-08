from datetime import date, timedelta
import locale
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from .models import Rol, Usuario, Producto, Direccion, Comuna, Categoria, Detalle, Compra

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

@login_required
def cart(request):
    return render(request, 'core/cart.html')

def search(request):
    return render(request, 'core/search.html')

def conf_pago(request):
    return render(request, 'core/conf_pago.html')

def create_acc(request):
    return render(request, 'core/create_acc.html')

@login_required
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

# ACTUALIZAR DE INFORMACION DE LA CUENTA
@login_required
def actualizarCuenta(request):
    correo_c = request.POST['correo']
    password_c = request.POST['password']

    # Actualizar el usuario actual
    Usuario.objects.filter(c_alias=request.user.username).update(
        c_correo=correo_c,
        c_password=password_c,
    )
    messages.add_message(request, messages.SUCCESS, '¡Su información se ha modificado exitosamente!')
    return redirect('userAcc')

# VISUALIZA LA INFO DE LA CUENTA
def userAcc(request):
    usuario = Usuario.objects.get(c_alias=request.user.username)
    context = {
        'usuario': usuario
    }
    return render(request, 'core/p_acc.html', context)

# ACTUALIZACION DEL PRODUCTO A LA BASE DE DATOS
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
    messages.add_message(request, messages.SUCCESS, '¡Su información se ha modificado exitosamente!')
    return redirect('userInfo')

# INGRESAR DE DIRECCION DEL USUARIO
@login_required
def registrarDir(request):
    usuariod = Usuario.objects.get(c_alias=request.user.username)
    d_calle = request.POST['calle']
    d_numero = request.POST['numero']
    d_comuna = request.POST['comuna']
    d_codigopostal = request.POST['codigo-postal']

    dr_comuna = Comuna.objects.get(com_nom = d_comuna)

    Direccion.objects.filter(usuario = usuariod.id_usuario).update(   
        dir_calle=d_calle,
        dir_numero=d_numero,
        comuna=dr_comuna.id_com,
        dir_cod_postal=d_codigopostal,
        usuario = usuariod.id_usuario
    )
    messages.add_message(request, messages.SUCCESS, '¡Su información se ha modificado exitosamente!')
    return redirect('userInfo') 
        
# VISUALIZA LA INFO DEL USUARIO
def userInfo(request):
    usuario = Usuario.objects.get(c_alias=request.user.username) 
    direccion = Direccion.objects.get(usuario = usuario.id_usuario) 
    context = {
        'usuario': usuario,
        'direccion': direccion,
        'comuna_seleccionada': direccion.comuna
    }
    return render(request, 'core/p_info.html', context)
    
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
    
    Direccion.objects.create(usuario = Usuario.objects.get(c_alias=alias_u), comuna = Comuna.objects.get(id_com=99))
    Compra.objects.create(usuario = Usuario.objects.get(c_alias=alias_u),
                          direccion = Direccion.objects.get(usuario = Usuario.objects.get(c_alias=alias_u)))
    
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
    user1 = request.POST['email']
    pass1 = request.POST['password']
    try:
        user = User.objects.get(username = user1)
    except User.DoesNotExist:
        print(1)
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect('index')

    pass_valid = check_password(pass1, user.password)
    if not pass_valid:
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect('index')
    
    user2 = Usuario.objects.get(c_alias=user1, c_password=pass1)
    user = authenticate(request, username=user1, password=pass1)
    
    if user is not None:
        login(request, user)
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

#PERMITE REGISTRAR DETALLE ASOCIADO A USUARIO CONECTADO
@login_required
def registrarDetalle(request, id_prod, precio):
    id_usuario  = request.user.id
    compra  = Compra.objects.get(usuario = id_usuario-1, cop_realizada=False)
    producto    = Producto.objects.get(id_prod = id_prod)
    dr_cantidad = request.POST['cantidad']
    dr_subtotal = precio * int(dr_cantidad)
    
    if (int(dr_cantidad)<producto.prod_stock):
        Detalle.objects.create(compra = compra, producto = producto, de_cantidad = dr_cantidad, de_subtotal = dr_subtotal)
        
        return redirect('search', 5)
    else:
        messages.add_message(request, messages.WARNING, 'La cantidad elegida supera el stock')
        return redirect('product1', id_prod)

#PERMITE MOSTRAR TODOS LOS DETALLES DEL USUARIO
@login_required
def cart(request):
    id_usuario = request.user.id
    compra  = Compra.objects.get(usuario = id_usuario-1, cop_realizada=False)
    detalle = Detalle.objects.filter(compra = compra)
    costo_envio = compra.direccion.comuna.com_cost_envio
    
    # Calcular subtotal
    subtotal = sum(d.de_subtotal for d in detalle)

    # Calcular impuesto
    impuesto = round(subtotal * 0.19)

    # Calcular total
    total = subtotal + impuesto + costo_envio
    
    contexto = {
        "listado": detalle,
        "subtotal": subtotal,
        "impuesto": impuesto,
        "costo_envio": costo_envio,
        "total": total
    }
    return render(request, 'core/cart.html',contexto)

#PERMITE ELIMINAR UN DETALLE
@login_required
def eliminarDetalle(request,id):
    detalle = Detalle.objects.get(id_detalle = id)
    detalle.delete()
    
    return redirect('cart')

#PERMITE REALIZAR LA COMPRA DE UN CARRITO, GUARDAR LA INFORMACIÓN Y CREAR UN CARRITO NUEVO 
@login_required
def realizarCompra(request, total):
    id_usuario  = request.user.id
    compra  = Compra.objects.get(usuario = id_usuario-1, cop_realizada=False)
    detalle = Detalle.objects.filter(compra = compra)
    
    c_usuario   = compra.usuario
    c_direccion = compra.direccion
    
    if detalle.exists():
        if (c_direccion.comuna.id_com != 99):
            costo_envio = compra.direccion.comuna.com_cost_envio
            costo_total = costo_envio + total
            flag_compra = True

            fecha_compra = date.today()
            fecha_despacho = date.today() + timedelta(days=7)
            
            costo_envio = compra.direccion.comuna.com_cost_envio
        
            compra.cop_fechcom  = fecha_compra
            compra.cop_fech_entr = fecha_despacho
            compra.com_cost_envio = costo_envio
            compra.cop_total    = costo_total
            compra.cop_realizada = flag_compra
            
            for i in detalle:
                i.producto.prod_stock = i.producto.prod_stock - i.de_cantidad
                
                i.producto.save()
            
            compra.save()
            
            Compra.objects.create(usuario = c_usuario, direccion = c_direccion)
            
            return redirect('h_buy')
        else:
            messages.add_message(request, messages.ERROR, 'Primero ingrese su información de dirección')
            return redirect('p_info')
    else:
        messages.add_message(request, messages.ERROR, 'El carrito no posee ningun producto')
        return redirect('cart')
        
#Lista las compras en la pagina h_buy/historial de compras
@login_required
def h_buy(request):
    id_usuario = request.user.id
    compra = Compra.objects.filter(usuario = id_usuario-1, cop_realizada=True)
    
    contexto = {
        "listado": compra
    }
    
    return render(request, 'core/h_buy.html', contexto)

@login_required
def h_prod1(request, id_com):
    id_usuario  = request.user.id
    compra  = Compra.objects.get(id_compra = id_com)
    detalle = Detalle.objects.filter(compra = compra)
    direccion   = compra.direccion
    costo_envio = compra.cop_total-compra.com_cost_envio
    
    contexto = {
        "listado": detalle,
        "compra": compra,
        "direccion": direccion,
        "costo_envio": costo_envio
    }
    return render(request, 'core/h_prod1.html',contexto)