from django.urls import path, include
from . import views

urlpatterns = [    
    path('lista/', views.listar_mascotas, name='mascota_listado'),   
    path('', views.inicio, name='mascota_inicio'),   
]
