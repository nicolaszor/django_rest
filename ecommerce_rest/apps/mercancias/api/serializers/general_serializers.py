from apps.mercancias.models import MeasureUnite,CategoryMercancia, Indicadores
from rest_framework import serializers

class MeasureUnitMercanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnite
        exclude = ("state","created_date","deleted_date","modifield_date")#aqui le ponemos que queremos que No muestre

class CategoryMercanciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMercancia
        exclude = ("state","created_date","deleted_date","modifield_date")

class IndicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicadores
        exclude = ("state","created_date","deleted_date","modifield_date")