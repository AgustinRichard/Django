from django.urls import path, include
from . import views

urlpatterns = [    
    path('listado/', views.listado, name='listado artículos'),   
    path('hardware/', views.hardware, name='listado hardware'),
    path('software/', views.software, name='listado software'),  
]
