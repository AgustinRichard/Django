from django.contrib import admin
from .models import Mascota

class MascotaAdm(admin.ModelAdmin):
    search_fields = ('nombre', 'dueño')

# Register your models here.

admin.site.register(Mascota, MascotaAdm)