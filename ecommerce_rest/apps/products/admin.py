from django.contrib import admin
from apps.products.models import *

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = {"id","descripcion"}

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = {"id","descripcion"}
    
admin.site.register(MeasureUnit)
admin.site.register(CategoryProduct)
admin.site.register(Indicador)
admin.site.register(Product)
# Register your models here.
