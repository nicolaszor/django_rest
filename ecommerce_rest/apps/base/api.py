from rest_framework import generics


class GeneralListApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)
        """
        //estamos generalizando codigo para no repetirnos en las bvvistas generales
        //get_serializer()metodo de generics
        //retorna lo que se define en la variable serializer class
        //el Meta.models le indica que ahi debe buscar el nombre del modelo
        """
        