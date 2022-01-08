from rest_framework import generics
from apps.base.api import GeneralListApiView
from rest_framework.response import Response
from rest_framework import status

from apps.products.api.serializers.product_serializers import ProductSerializer
"""
//Esta clase no nos sirve, porque ya la agregamos al createapiview

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer
"""

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state = True)#con listcreateapiview tenemos tambien metodo get y no solo post


    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Producto creado correctamente!"},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):#le agregamos el update y el destroy al retrieve para poder actualizar y eliminar lo que recuperamos
    serializer_class = ProductSerializer
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state= True)#le dice donde buscar para comparar el pk con el id
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk,state= True).first()
        
        """
        para sobre escribir esto tendriamos que utilizar
        def get(self,request,pk=none)
        como lo hicimos en User
        """

    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return Response({"Error":"No existe un producto con estos datos"},status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None ):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)#self.get_queryset es la instancia 
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False #en ves de eliminarlo de la base de datos le cambiamos el estado a FALSE para poder seguirlo viendo desde admin y que no se borre de la base de datos
            product.save()#esto se llama eliminacion logica

            return Response({"message":"Producto eliminado correctamente"},status=status.HTTP_200_OK)
        return Response({"Error":"No existe un producto con estos datos"},status = status.HTTP_400_BAD_REQUEST)



"""
//Unimos estas vistas arriba
//sacamos y copiamos los metodos y nos ahorramos vistas y urls


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state= True)#le ponemos el estado en true si esta en false no lo va a encontrar 
      
        //Esta eliminaciones una directa lo elimina de la base de datos
        //Para evitar esto vamos a sobre escribir el metodo delete
      

    def delete(self,request,pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False #en ves de eliminarlo de la base de datos le cambiamos el estado a FALSE para poder seguirlo viendo desde admin y que no se borre de la base de datos
            product.save()#esto se llama eliminacion logica

            return Response({"message":"Producto eliminado correctamente"},status=status.HTTP_200_OK)
        return Response({"Error":"No existe un producto con estos datos"},status = status.HTTP_400_BAD_REQUEST)

class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state= True).filter(id=pk).first()

    #def patch(self)#patch es el metodo que tiene django para obtener la data vieja(la instancia)a actualizar
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return Response({"Error":"No existe un producto con estos datos"},status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None ):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)#self.get_queryset es la instancia 
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""