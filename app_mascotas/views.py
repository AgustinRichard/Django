from django.shortcuts import render, HttpResponse
from .models import Mascota

# Create your views here.
def listar_mascotas(request):
        
    lista_mascotas = Mascota.objects.all()
    
    return render(request, 'app_mascotas/listado.html',
                    {
                 'mensajito': 'veterinaria pipo', 
                 'lista': lista_mascotas,                
                }
    )

def inicio(request):
    return render(request, 
                'app_mascotas/inicio.html'
                )
