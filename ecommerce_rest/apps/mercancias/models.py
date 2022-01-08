from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class MeasureUnite(BaseModel):
    description = models.CharField("Descripcion", max_length=50,blank=False,null=False,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
        return self.description

class CategoryMercancia(BaseModel):
    description = models.CharField("Descripcion", max_length=50,blank=False,null=False,unique=True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de Mercancia"
        verbose_name_plural = "Categorias de Mercancias"

    def __str__(self):
        return self.description


class Indicadores(BaseModel):
    historical = HistoricalRecords()
    category_mercancia = models.ForeignKey(CategoryMercancia,on_delete= models.CASCADE, verbose_name = "Indicador de oferta")
    descount_value = models.PositiveIntegerField(default=0)


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "indicador de oferta"
        verbose_name_plural = "indicadores de ofertas"

    def __str__(self):
        return f"oferta de la categoria {self.category_product}:{self.descount_value}%"

class Mercancia(BaseModel):
    historical = HistoricalRecords()
    name = models.CharField("Nombre del mercancia", max_length=150,unique=True,blank=False,null=False)
    description = models.TextField("Descripcion de mercancia", max_length=150,blank=False,null=False)
    image = models.ImageField("Imagen de la mercancia", upload_to= "mercancia/",blank = True,null=True)
    measure_unite = models.ForeignKey(MeasureUnite,on_delete= models.CASCADE, verbose_name = "Unidad de medida",null = True)
    category_mercancia =models.ForeignKey(CategoryMercancia,on_delete= models.CASCADE, verbose_name = "categoria de la mercancia",null = True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Mercancia"
        verbose_name_plural = "Mercancias"

    def __str__(self):
        return self.name

