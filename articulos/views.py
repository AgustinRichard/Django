from django.shortcuts import render
from .models import Articulo

# Create your views here.
def listado(request):
    lista_articulos = Articulo.objects.all()

    return render(request, 'articulos/List.html', {'nombre': 'artículos', 'lista': lista_articulos})

def hardware(request):
    lista_hardware = Articulo.objects.filter(categoria="hardware")

    return render(request, 'articulos/List.html', {'nombre': 'hardware', 'lista':lista_hardware})

def software(request):
    lista_software = Articulo.objects.filter(categoria="software")

    return render(request, 'articulos/List.html', {'nombre': 'software', 'lista':lista_software})