from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#vistas

"""
class UserAPIView(APIView):
    def get(salf,request):
        users = User.objects.all()
        users_serializers = UserSerializer(users, many = True)#many igual true es para avisar al serializador que se le entrega un listado y no un solo objeto
        return Response(users_serializers.data)#data es un atributo con los datos del serializador
"""


#lo mismo de arriba con un decorador
@api_view(["GET", "POST"])#el decorador toma una lista con los metodos permitidos
def user_api_view(request):
    #list
    if request.method == "GET":
        users = User.objects.all().values("id","username","email","password")
        users_serializers = UserListSerializer(users, many = True)
        #utilizando serializador creado a mano
        """
        test_data = {
            "name": "develop",
            "email": "develop@hotmail.com"
        }

        test_user = TestUserSerializer(data = test_data, context =test_data)#de esta manera pasa todo el dic a cada serializador para tener disponible toda la data.
        if test_user.is_valid():
            user_instance = test_user.save()#es lo que validamos en def create() serializer 
            print(user_instance)
        else:
            print(test_user.errors)
        """
        return Response(users_serializers.data, status= status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        users_serializer = UserSerializer(data = request.data)#asocia el request con el modelo y lo valida
        #validacion:
        if users_serializer.is_valid():#si la serializacion es valida
            users_serializer.save()#este save() afecta al serializador,verifica si hay un metodo en el serializador
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(users_serializer.errors)


@api_view(["GET","PUT","DELETE"])
def user_detail_api_view(request,pk= None):
    #queryset
    user = User.objects.filter(id = pk).first()
    #validacion
    if user:
        #retrieve
        if request.method == "GET":
            #user = User.objects.filter(id = pk).first()
            users_serializer = UserSerializer(user)
            return Response(users_serializer.data,status=status.HTTP_200_OK)
        #update
        elif request.method == "PUT":
            #user = User.objects.filter(id = pk).first()
            users_serializer = UserSerializer(user,data = request.data)#pasamos la isntancia user mas la data de esta manera sabe que vamos a actualizar
            if users_serializer.is_valid():
                users_serializer.save()
                return Response(users_serializer.data,status= status.HTTP_200_OK)
            return Response(users_serializer.error, status=status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == "DELETE":
            #user = User.objects.filter(id = pk).first() para no repetir la consulta lo validamos arriba
            user.delete()
            return Response({"message": "Usuario eliminado correctamente"}, status= status.HTTP_200_OK)

    return Response({"message": "no se econtro ningun dato"}, status=status.HTTP_400_BAD_REQUEST)

