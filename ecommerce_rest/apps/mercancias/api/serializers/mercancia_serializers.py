from rest_framework import serializers#primero importamos lo que le pertenece a django

from apps.mercancias.models import Mercancia




class MercanciaSerializer(serializers.ModelSerializer):
    """
    //De esta manera estableciendo los campos measure_unite y category_product
    igual que como se encuentran en el modelo product 
    //nos devuelve lo que esta definido en el 
    __str__ de cada uno y NO el id de la clave foranea
    

    measure_unite = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()
    """    
    class Meta:
        model = Mercancia
        exclude = ("state","created_date","deleted_date","modifield_date")

        """como mostrar los campos de manera mas simple que la de arriba"""

    def validate_meassure_unite(self,value):
        if value == "" or value == None:
            raise serializers.ValidationError("Debe ingresar una unidad de medida")
        return value
    
    def validate_category_product(self, value):
        if value == "" or value == None:
            raise serializers.ValidationError("Debe ingresar una categoria valida")
        return value

    def to_representation(self,instance):
        return {
            "id": instance.id,
            "name":instance.name,
            "description": instance.description,
            "image": instance.image.url if instance.image != "" else "",#validamos que si la imagen es null devuelva una lista vacia
            "measure_unit":instance.measure_unite.description if instance.measure_unite != None else "",#le indicamos donde se encuentra en el modelo
            "category_mercancia":instance.category_mercancia.description if instance.category_mercancia != None else "",
        }