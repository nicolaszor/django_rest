from apps.base.api import GeneralListApiView
from apps.mercancias.api.serializers.general_serializers import MeasureUnitMercanciaSerializer, IndicadoresSerializer,CategoryMercanciasSerializer

from rest_framework import viewsets

class MeasureUnitListAPIView(viewsets.ModelViewSet):#al eredar de listAPIview ya sabe que solo acepta get
    """
        dejamos un comentario de esta manera para verlo en la documentacion
    """
    
    serializer_class = MeasureUnitMercanciaSerializer #de que serializardor toma
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state= True)#le dice donde buscar para comparar el pk con el id
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk,state= True).first()
  
    """
    //esto lo deveriamos hacer si no utilizariamos GeneralListApiView y heredaramos de 
    generics.ListAPIView
    si el comentario esta en el metodo sea create(),destroy() list() etc
    toma ese sino toma el de la clase general como MeasureUnitListAPIView
    
    """    

class CategoryMercanciaUnitListAPIView(viewsets.ModelViewSet):#al eredar de listAPIview ya sabe que solo acepta get
    serializer_class = CategoryMercanciasSerializer #de que serializardor toma
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state= True)#le dice donde buscar para comparar el pk con el id
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk,state= True).first()

class IndicadorListAPIView(viewsets.ModelViewSet):#al eredar de listAPIview ya sabe que solo acepta get
    serializer_class = IndicadoresSerializer #de que serializardor toma
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state= True)#le dice donde buscar para comparar el pk con el id
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk,state= True).first()
