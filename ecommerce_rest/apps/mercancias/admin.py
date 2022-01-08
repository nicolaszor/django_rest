from django.contrib import admin

# Register your models here.
from django.contrib import admin
from apps.mercancias.models import *

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = {"id","descripcion"}

class CategoryMercanciaAdmin(admin.ModelAdmin):
    list_display = {"id","descripcion"}
    
admin.site.register(MeasureUnite)
admin.site.register(CategoryMercancia)
admin.site.register(Indicadores)
admin.site.register(Mercancia)