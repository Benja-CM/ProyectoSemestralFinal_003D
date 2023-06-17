from datetime import date, timedelta
import locale
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from .models import Rol, Usuario, Producto, Direccion, Comuna, Categoria, Detalle, Compra
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request, 'core/Index.html')

def product(request):
    return render(request, 'core/product1.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'core/profile.html')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

def cart(request):
    if request.user.is_authenticated:
        return render(request, 'core/cart.html')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

def search(request):
    return render(request, 'core/search.html')

def conf_pago(request):
    return render(request, 'core/conf_pago.html')

def create_acc(request):
    return render(request, 'core/create_acc.html')

def h_buy(request):
    if request.user.is_authenticated:
        return render(request, 'core/h_buy.html')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

def h_prod1(request):
    if request.user.is_authenticated:
        return render(request, 'core/h_prod1.html')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

def p_acc(request):
    return render(request, 'core/p_acc.html')

def p_info(request):
    return render(request, 'core/p_info.html')

def pss_fg(request):
    return render(request, 'core/pss_fg.html')

def vent_ing(request):
    return render(request, 'core/vent_ing.html')

def vend_create(request):
    if request.user.is_authenticated:
        if request.session.get('lvl') == 'Vendedor':
            return render(request, 'core/vend_create.html')
        else:
            messages.warning(request,'Debe ser un vendedor para acceder a esta pagina')
            return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')


# PERMITE EDITAR UN PRODUCTO SELECCIONADO DE LA LISTA
def vent_edit(request, id):
    if request.user.is_authenticated:
        if request.session.get('lvl') == 'Vendedor':
            categorias = Categoria.objects.all()
            producto = Producto.objects.get(id_prod = id)
            contexto = {
                "datos": producto,
                "listaCategorias": categorias
            }
            
            return render(request, 'core/vent_edit.html', contexto)
        else:
            messages.warning(request,'Debe ser un vendedor para acceder a esta pagina')
            return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

# LISTA LOS PRODUCTOS DE LA BASE DE DATOS
def vent_list(request):
    if request.user.is_authenticated:
        if request.session.get('lvl') == 'Vendedor':
            productos = Producto.objects.all()
            contexto = {
                "listado": productos
            }
            return render(request, 'core/vent_list.html',contexto)
        else:
            messages.warning(request,'Debe ser un vendedor para acceder a esta pagina')
            return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

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

#BUSCADOR DE PRODUCTOS COMO CLIENTE
def buscar(request):
    buscar = request.POST['buscar']
    productos = Producto.objects.filter(prod_nom__icontains=buscar)
    
    contexto = {
        "listado": productos
    }
    
    return render(request, 'core/search.html', contexto)

#BUSCADOR DE PRODUCTOS PARA LISTAR Y MODIFICAR
def buscarProd(request):
    buscar = request.POST['buscar']
    productos = Producto.objects.filter(prod_nom__icontains=buscar)
    
    contexto = {
        "listado": productos
    }
    
    return render(request, 'core/vent_list.html', contexto)

# ACTUALIZAR DE INFORMACION DE LA CUENTA
def actualizarCuenta(request):
    if request.user.is_authenticated:
        correo_c = request.POST['correo']
        password_c = request.POST['password']

        # Actualizar el usuario actual
        Usuario.objects.filter(c_alias=request.user.username).update(
            c_correo=correo_c,
            c_password=password_c,
        )
        # Obtén el objeto del usuario
        user = User.objects.get(username=request.user.username)

        # Actualiza los campos del usuario
        user.email = correo_c

        # Encripta la nueva contraseña antes de actualizarla
        if password_c:
            user.password = make_password(password_c)

        # Guarda los cambios en la base de datos
        user.save()

        messages.success(request,'¡Su información se ha modificado exitosamente!')
        return redirect('userAcc')
    else:
        messages.warning(request,'Por favor, inicie sesión')
        return redirect('index')

# VISUALIZA LA INFO DE LA CUENTA
def userAcc(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(c_alias=request.user.username)
        context = {
            'usuario': usuario
        }
        return render(request, 'core/p_acc.html', context)
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

# INGRESAR INFORMACION DE CUENTA
def registrarInfAC(request):
    alias_u = request.POST['alias']
    correo_u = request.POST['email']
    password_u = request.POST['password']
    rol_u = 1
    role = Rol.objects.get(id_rol=rol_u)

    if User.objects.filter(username=alias_u).exists():
        messages.error(request,'El nombre de usuario ya está ocupado. Por favor, elige otro nombre')
        return redirect('create_acc')

    if Usuario.objects.filter(c_alias=alias_u).exists():
        messages.error(request,'El nombre de usuario ya está ocupado. Por favor, elige otro nombre')
        return redirect('create_acc')
    
    if User.objects.filter(email=correo_u).exists():
        messages.error(request, 'El correo electrónico ya está registrado. Por favor, utiliza otro correo.')
        return redirect('create_acc')
    
    if Usuario.objects.filter(c_correo=correo_u).exists():
        messages.error(request, 'El correo electrónico ya está registrado. Por favor, utiliza otro correo.')
        return redirect('create_acc')

    Usuario.objects.create(c_alias=alias_u, c_correo=correo_u, c_password=password_u, rol=role)
    user = User.objects.create_user(username=alias_u, email=correo_u, password=password_u)
    user.is_active = True
    user.is_staff = False
    user.save()
    
    Direccion.objects.create(usuario = Usuario.objects.get(c_alias=alias_u), comuna = Comuna.objects.get(id_com=99))
    Compra.objects.create(usuario = Usuario.objects.get(c_alias=alias_u),
                          direccion = Direccion.objects.get(usuario = Usuario.objects.get(c_alias=alias_u)))
    
    messages.success(request, '¡La cuenta se ha creado exitosamente!')

    return redirect('index')

# INGRESAR INFORMACION DE CUENTA DE VENDEDOR
def registrarVendAcc(request):
    if request.user.is_authenticated:
        alias_u = request.POST['alias']
        correo_u = request.POST['email']
        password_u = request.POST['password']
        rol_u = 2
        role = Rol.objects.get(id_rol=rol_u)

        if User.objects.filter(username=alias_u).exists():
            messages.error(request,'El nombre de usuario ya está ocupado. Por favor, elige otro nombre')
            return redirect('vend_create')

        if Usuario.objects.filter(c_alias=alias_u).exists():
            messages.error(request,'El nombre de usuario ya está ocupado. Por favor, elige otro nombre')
            return redirect('vend_create')
        
        if User.objects.filter(email=correo_u).exists():
            messages.error(request, 'El correo electrónico ya está registrado. Por favor, utiliza otro correo.')
            return redirect('vend_create')
        
        if Usuario.objects.filter(c_correo=correo_u).exists():
            messages.error(request, 'El correo electrónico ya está registrado. Por favor, utiliza otro correo.')
            return redirect('vend_create')

        Usuario.objects.create(c_alias=alias_u, c_correo=correo_u, c_password=password_u, rol=role)
        user = User.objects.create_user(username=alias_u, email=correo_u, password=password_u)
        user.is_active = True
        user.is_staff = False
        user.save()
        
        Direccion.objects.create(usuario = Usuario.objects.get(c_alias=alias_u), comuna = Comuna.objects.get(id_com=99))
        Compra.objects.create(usuario = Usuario.objects.get(c_alias=alias_u),
                            direccion = Direccion.objects.get(usuario = Usuario.objects.get(c_alias=alias_u)))
        
        messages.success(request, '¡La cuenta se ha creado exitosamente!')

        return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

# INGRESAR DE INFORMACION DEL USUARIO
def registrarInfUS(request):
    if request.user.is_authenticated:
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

        messages.success(request, '¡Su información se ha modificado exitosamente!')

        return redirect('userInfo')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

# INGRESAR DE DIRECCION DEL USUARIO
def registrarDir(request):
    if request.user.is_authenticated:
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
        messages.success(request, '¡Su información de dirección se ha modificado exitosamente!')
        return redirect('userInfo') 
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')
        
# VISUALIZA LA INFO DEL USUARIO
def userInfo(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(c_alias=request.user.username)
         
        direccion = Direccion.objects.get(usuario = usuario.id_usuario) 
        context = {
            'usuario': usuario,
            'direccion': direccion,
            'comuna_seleccionada': direccion.comuna
        }
        return render(request, 'core/p_info.html', context)
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')
    
# INGRESAR DE PRODUCTOS
def registrarProducto(request):
    if request.user.is_authenticated:
        if request.session.get('lvl') == 'Vendedor':
            pr_nom      = request.POST['nombre']
            pr_descripcion = request.POST['desc']
            pr_precio   = request.POST['precio']
            pr_stock    = request.POST['stock']
            pr_imagen   = request.FILES['imagen']
            pr_cat      = request.POST['sa-cat']

            registroCat = Categoria.objects.get(id_cat = pr_cat)

            Producto.objects.create(prod_nom = pr_nom, prod_descripcion = pr_descripcion, prod_precio = pr_precio,
                                prod_stock = pr_stock, prod_imagen = pr_imagen, categoria = registroCat)
            
            messages.success(request, 'El producto se ha agregado correctamente.')

            return redirect('vent_list')
        else:
            messages.warning(request,'Debe ser un vendedor para acceder a esta pagina')
            return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

# ACTUALIZACION DEL PRODUCTO A LA BASE DE DATOS
def actualizarProducto(request):
    if request.user.is_authenticated:
        if request.session.get('lvl') == 'Vendedor':
            id      = request.POST['ID']
            nombre  = request.POST['nombre']
            descripcion = request.POST['desc']
            precio  = request.POST['precio']
            stock   = request.POST['stock']
            categoria   = request.POST['categoria']

            producto = Producto.objects.get(id_prod = id)
            producto.prod_nom = nombre
            producto.prod_descripcion = descripcion
            producto.prod_precio = precio
            producto.prod_stock = stock
            
            registroCategoria = Categoria.objects.get(id_cat = categoria)
            producto.categoria = registroCategoria
            
            if bool(request.FILES.get('imagen')):
                imagen  = request.FILES['imagen']
                producto.prod_imagen = imagen
                producto.save()
            else:
                Producto.objects.filter(id_prod=id).update(
                    prod_nom = nombre,
                    prod_descripcion = descripcion,
                    prod_precio = precio,
                    prod_stock = stock,
                    categoria = categoria
                )
                
            messages.success(request, '¡El producto se ha modificado exitosamente!')
            return redirect('vent_list')
        else:
            messages.warning(request,'Debe ser un vendedor para acceder a esta pagina')
            return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

# ELIMINAR PRODUCTOS DE LA BASE DE DATOS
def eliminarProducto(request,id):
    if request.user.is_authenticated:
        if request.session.get('lvl') == 'Vendedor':
            producto = Producto.objects.get(id_prod = id)
            producto.delete()
            
            messages.success(request, '¡El producto se ha eliminado exitosamente!')

            return redirect('vent_list')
        else:
            messages.warning(request,'Debe ser un vendedor para acceder a esta pagina')
            return redirect('profile')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

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
        messages.add_message(request, messages.ERROR, 'El usuario o la contraseña son incorrectos')
        return redirect('index')

    pass_valid = check_password(pass1, user.password)
    if not pass_valid:
        messages.add_message(request, messages.ERROR, 'El usuario o la contraseña son incorrectos')
        return redirect('index')
    
    user2 = Usuario.objects.get(c_alias=user1, c_password=pass1)
    user = authenticate(request, username=user1, password=pass1)
    
    if user is not None:
        login(request, user)
        if user2.rol.id_rol == 1:
            request.session['lvl'] = 'Cliente'
            return redirect('profile')
        if user2.rol.id_rol == 2:
            request.session['lvl'] = 'Vendedor'
            print(request.session.get('lvl'))
            return redirect('profile')
    else:
        print("8")
    
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

#PERMITE REGISTRAR DETALLE ASOCIADO A USUARIO CONECTADO
def registrarDetalle(request, id_prod, precio):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(c_alias=request.user)
        c_usuario = usuario.id_usuario
        
        compra  = Compra.objects.get(usuario=c_usuario, cop_realizada=False)
        
        producto    = Producto.objects.get(id_prod = id_prod)
        dr_cantidad = request.POST['cantidad']
        stock   = int(dr_cantidad)
        
        dr_subtotal = precio * stock
        
        if (stock<=producto.prod_stock):
            Detalle.objects.create(compra = compra, producto = producto, de_cantidad = stock, de_subtotal = dr_subtotal)
            messages.success(request, '¡El producto se ha agregado al carrito!')
            
            producto.prod_stock = producto.prod_stock-stock
            producto.save()
            
            if (request.POST['action'] == 'agregar'):
                return redirect('search', 5)
            elif (request.POST['action'] == 'comprar'):
                return redirect('cart')
            else:
                messages.error(request, 'Opción invalida')
        else:
            messages.warning(request, 'La cantidad solicitada supera el stock disponible.')
            return redirect('product1', id_prod)
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

#PERMITE MOSTRAR TODOS LOS DETALLES DEL USUARIO
def cart(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(c_alias=request.user)
        id_usuario = usuario.id_usuario
        compra = Compra.objects.get(usuario=id_usuario, cop_realizada=False)
        
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
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

#PERMITE ELIMINAR UN DETALLE
def eliminarDetalle(request,id):
    if request.user.is_authenticated:
        detalle = Detalle.objects.get(id_detalle = id)
        id_prod = detalle.producto.id_prod
        prod    = Producto.objects.get(id_prod = id_prod)
        
        prod.prod_stock = prod.prod_stock + detalle.de_cantidad
        
        prod.save()
        detalle.delete()
        
        messages.success(request,'Se eliminó el detalle del carrito')
        return redirect('cart')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

#PERMITE REALIZAR LA COMPRA DE UN CARRITO, GUARDAR LA INFORMACIÓN Y CREAR UN CARRITO NUEVO 
def realizarCompra(request, total):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(c_alias=request.user)
        c_usuario = usuario.id_usuario
        
        compra  = Compra.objects.get(usuario=c_usuario, cop_realizada=False)
        detalle = Detalle.objects.filter(compra=compra)
        
        c_direccion = compra.direccion
        
        if detalle.exists():
            if (c_direccion.comuna.id_com != 99):
                costo_envio = compra.direccion.comuna.com_cost_envio
                flag_compra = True

                fecha_compra = date.today()
                fecha_despacho = date.today() + timedelta(days=7)
                
                costo_envio = compra.direccion.comuna.com_cost_envio
            
                compra.cop_fechcom  = fecha_compra
                compra.cop_fech_entr = fecha_despacho
                compra.com_cost_envio = costo_envio
                compra.cop_total    = total
                compra.cop_realizada = flag_compra
                
                Compra.objects.create(usuario = usuario, direccion = c_direccion)
                
                compra.save()
                
                messages.success(request, '¡La compra se ha realizado exitosamente!')
                return redirect('h_buy')
            else:
                messages.error(request, 'Primero ingrese su información de dirección')
                return redirect('p_info')
        else:
            messages.warning(request,'El carrito no posee ningun producto')
            return redirect('cart')
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')
        
#Lista las compras en la pagina h_buy/historial de compras
def h_buy(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(c_alias=request.user)
        id_usuario = usuario.id_usuario
        compra = Compra.objects.filter(usuario=id_usuario, cop_realizada=True)
        
        contexto = {
            "listado": compra
        }
        
        return render(request, 'core/h_buy.html', contexto)
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')

#LISTA LOS DETALLES DE UNA COMPRA
def h_prod1(request, id_com):
    if request.user.is_authenticated:
        id_usuario  = request.user.id
        compra  = Compra.objects.get(id_compra = id_com)
        detalle = Detalle.objects.filter(compra = compra)
        direccion   = compra.direccion
        costo_sin_envio = compra.cop_total-compra.com_cost_envio
        
        subtotal = sum(d.de_subtotal for d in detalle)

        # Calcular impuesto
        impuesto = round(subtotal * 0.19)
        
        contexto = {
            "listado": detalle,
            "compra": compra,
            "direccion": direccion,
            "subtotal": subtotal,
            "impuesto": impuesto
        }
        return render(request, 'core/h_prod1.html',contexto)
    else:
        messages.warning(request,'Debe estar registrado para acceder a esta pagina')
        return redirect('index')
 
def error_404(request, exception):
    return render(request, 'core/404.html')