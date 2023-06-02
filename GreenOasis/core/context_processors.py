from .models import Categoria

# LISTA LAS CAREGORIAS DE LA BASE DE DATOS
def categorias_context_processor(request):
    c = Categoria.objects.all()
    return {'listaCategorias': c}