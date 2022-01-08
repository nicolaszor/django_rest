from rest_framework import generics
from apps.base.api import GeneralListApiView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.mercancias.api.serializers.mercancia_serializers import MercanciaSerializer
from apps.users.autentication_mixin import Authentication
from rest_framework.parsers import JSONParser, MultiPartParser
#from rest_framework.permissions import IsAuthenticated esto lo hacemos si queremos autenticar vistas particulares y no glovales
"""
//Los viewset unen el CRUD completo en 1 clase
//Podemos sobre escribir cualquier metodo
//create(),put(),destroy(),list(),queryset(),save(),etc..
//o dejarlo como esta y ya funciona
"""

class MercanciaViewSet(viewsets.ModelViewSet):#antes heredamos de Authentication primero, ahora que la convertimos en clase gloval no hace falta >>(viejo)
    serializer_class = MercanciaSerializer
    parser_classes = (JSONParser, MultiPartParser, )
    #permission_classes = (IsAuthenticated,)# esto lo hacemos para que realize las validaciones, esto debemos definirlo en cada vista que nec la validacion de token
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state= True)#le dice donde buscar para comparar el pk con el id
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk,state= True).first()

    def list(self,request):
        print(request.user)#usuario actual
        mercancia_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(mercancia_serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Mercancia creada correctamente!"},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk = None):
        mercancia = self.get_queryset().filter(id = pk).first()
        if mercancia:
            mercancia.state = False #en ves de eliminarlo de la base de datos le cambiamos el estado a FALSE para poder seguirlo viendo desde admin y que no se borre de la base de datos
            mercancia.save()#esto se llama eliminacion logica

            return Response({"message":"mercancia eliminado correctamente"},status=status.HTTP_200_OK)
        return Response({"Error":"No existe un mercancia con estos datos"},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk= None):
        if self.get_queryset(pk):
            mercancia_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)#self.get_queryset es la instancia 
            if mercancia_serializer.is_valid():
                mercancia_serializer.save()
                return Response(mercancia_serializer.data,status=status.HTTP_200_OK)
            return Response(mercancia_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


