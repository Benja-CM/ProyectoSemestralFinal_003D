from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/Index.html')

def product(request):
    return render(request, 'core/product1.html')

def profile(request):
    return render(request, 'core/profile.html')