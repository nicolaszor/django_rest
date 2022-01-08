#from rest_framework import generics
#from apps.products.models import MeasureUnit, Indicador, CategoryProduct
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicadorSerializer,CategoryProductSerializer



class MeasureUnitListAPIView(GeneralListApiView):#al eredar de listAPIview ya sabe que solo acepta get
    serializer_class = MeasureUnitSerializer #de que serializardor toma
    """
    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)

    //esto lo deveriamos hacer si no utilizariamos GeneralListApiView y heredaramos de 
    generics.ListAPIView

    """    

class CategoryProductUnitListAPIView(GeneralListApiView):#al eredar de listAPIview ya sabe que solo acepta get
    serializer_class = CategoryProductSerializer #de que serializardor toma

class IndicadorListAPIView(GeneralListApiView):#al eredar de listAPIview ya sabe que solo acepta get
    serializer_class = IndicadorSerializer #de que serializardor toma
