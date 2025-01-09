from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Color, Acabado, Carrusel, Bajoquinto  

def home(request):
    carrusel = Carrusel.objects.prefetch_related('imagenes').first()
    return render(request, 'home.html', {'carrusel': carrusel})


def about(request):
    return render(request, 'about.html')


def products(request):
    guitarras = Bajoquinto.objects.all()
    colores = Color.objects.all()

    min_price = request.GET.get('price_min')
    max_price = request.GET.get('price_max')
    search = request.GET.get('search')
    color = request.GET.get('color')
    curves = request.GET.get('curves')

    if search:
        guitarras = guitarras.filter(nombre__icontains=search)
    if min_price:
        guitarras = guitarras.filter(precio__gte=min_price)
    if max_price:
        guitarras = guitarras.filter(precio__lte=max_price)
    if color:
        guitarras = guitarras.filter(color__nombre=color)
    if curves:
        guitarras = guitarras.filter(curvas=curves)



    paginator = Paginator(guitarras, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'guitarras': page_obj, 
        'colores': colores,
    }

    return render(request, 'products.html', context)


def guitar_detail(request, id):
    guitarra = get_object_or_404(Bajoquinto, id=id) 

    return render(request, 'detalles_guitarra.html', {
        'guitarra': guitarra})

