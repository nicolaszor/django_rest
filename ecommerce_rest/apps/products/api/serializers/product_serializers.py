from rest_framework import serializers#primero importamos lo que le pertenece a django

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer



class ProductSerializer(serializers.ModelSerializer):
    """
    //De esta manera estableciendo los campos measure_unite y category_product
    igual que como se encuentran en el modelo product 
    //nos devuelve lo que esta definido en el 
    __str__ de cada uno y NO el id de la clave foranea
    

    measure_unite = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()
    """    
    class Meta:
        model = Product
        exclude = ("state","created_date","deleted_date","modifield_date")

        """como mostrar los campos de manera mas simple que la de arriba"""

    def to_representation(self,instance):
        return {
            "id": instance.id,
            "name":instance.name,
            "description": instance.description,
            "image": instance.image if instance.image != "" else "",#validamos que si la imagen es null devuelva una lista vacia
            "measure_unit":instance.measure_unite.description if instance.measure_unite != None else "",#le indicamos donde se encuentra en el modelo
            "category_product":instance.category_product.description if instance.category_product != None else "",
        }