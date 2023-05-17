from django.shortcuts import render

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

def vent_ing(request):
    return render(request, 'core/vent_ing.html')

def vent_list(request):
    return render(request, 'core/vent_list.html')