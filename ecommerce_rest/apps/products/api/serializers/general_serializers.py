

from apps.products.models import MeasureUnit,CategoryProduct, Indicador
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ("state","created_date","deleted_date","modifield_date")#aqui le ponemos que queremos que No muestre

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ("state","created_date","deleted_date","modifield_date")

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        exclude = ("state","created_date","deleted_date","modifield_date")


