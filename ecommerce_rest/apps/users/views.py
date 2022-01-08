from datetime import datetime
from rest_framework.views import APIView
from django.contrib.auth import authenticate # devuelve true o false si existe un usuario que coincida 
from django.contrib.sessions.models import Session #maneja las seciones
from rest_framework.generics import GenericAPIView
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken # esta clase recive un usuario como parametro y lo vuelve a generar un toquen
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
#from apps.users.api.serializers import UserTokenSerializer
#from apps.users.autentication_mixin import Authentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .api.serializers import CustomTokenObtainPairSerializer,CustomUserSerializer

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer #nombre que queramos
    def post(self,request,*args,**kwargs):
        username =request.data.get("username","")# si no encuentra el usuario envia cadena vacia
        password = request.data.get("password","")
        user = authenticate(
            username = username,
            password = password,
        )
        if user:
            login_serializer = self.serializer_class(data= request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    "token": login_serializer.validated_data.get("access"),
                    "refresh-token" : login_serializer.validated_data.get("refresh"),
                    "user" : user_serializer.data,
                    "message": "Inicio de seccion exitoso",
                },status=status.HTTP_200_OK )
            return Response({"error": "Contraceña o nombre de usuario incorrecto"},status=status.HTTP_400_BAD_REQUEST)


        return Response({"error": "Contraceña o nombre de usuario incorrecto"},status=status.HTTP_400_BAD_REQUEST)



class Logout(GenericAPIView):
    def post(self,request,*args,**kwargs):
        user = User.objects.filter(id = request.data.get("user",0).first())
        if user.exists():
            RefreshToken.for_user(user.first())#crea un nuevo token de acceso para el usuario indicado
            return Response({"message": "Seccion cerrada correctamente"},status=status.HTTP_200_OK)
        return Response({"error": "No existe el usuario"},status=status.HTTP_400_BAD_REQUEST)


"""
Esto ya no lo utlizamos dado que empesamos a usar la autenticacion por JWT

class UserToken(Authentication,APIView):#refrescar el token cuando expired = True y nos muestra el token actual de la base de datos asociado con el usuario
    def get(self,request,*args,**kwargs):
        print(self.user)
        username = request.GET.get("username")
        try:
            user_token = Token.objects.get(user = UserTokenSerializer().Meta.model.objects.filter(username = username).first())
            return Response(
                {
                    "token" : user_token.key
                }
            )
        except:
            return Response({
                "error": "Credenciales incorrectas."
            },status=status.HTTP_400_BAD_REQUEST)




class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data = request.data,context = {"request": request})#esta clase ya esta definida en ObtainAuthToken//este serializador tiene un campo llamado username y una llamdo password
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]#obtenemos el usuario
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)#si el usuario esta activo creamos el toquen y lo relacionamos con el
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        "token": token.key,
                        "user": user_serializer.data,
                        "message": "inicio de secion exitoso",
                    },status=status.HTTP_201_CREATED)


                    
                    //Este else de abajo cierra la session cuando se abre una nueva desde otro ordenador...
                    //si ya hay un toquen creado
                    //le borramos todas las sessiones activas
                   
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())#todas las sessiones que su tiempo de expiracion sea mayor igual que la hora actual
                    if all_sessions.exists():
                        for session in all_sessions:#busca en todas las sessiones aquella que corresponda con el usuario actual
                            session_data = session.get_decoded()
                            if user.id ==int(session_data.get("_auth_user_id")):#_auth_user_id es el id al cual corresponde la session,la igualamos con el id del usuario
                                session.delete()#borra la session ,te cierra la sessiones activas 
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        "token": token.key,
                        "user": user_serializer.data,
                        "message": "inicio de secion exitoso",
                    },status=status.HTTP_201_CREATED)#si ya tenia token lo elimina y crea otro sin que el usuario lo sepa
          
                    
                    //Otro caso si no queremos dejar ingresar al usuario pq ya otro inicio session
                
                   
            
                else:
                    token.delete()
                    return Response({"error":"Otro usuario ya inicio session"},status=status.HTTP_409_CONFLICT)

            else:
                return Response({"error": "Este usuario no puede iniciar sesion"},status=status.HTTP_401_UNAUTHORIZED)
        
        else:
             return Response({"error": "nombre de usuario o contraceña incorrecto"},status=status.HTTP_400_BAD_REQUEST)
        
        
        return Response({"mensaje": "hola desde response"},status=status.HTTP_200_OK)

class Logouter(APIView):

    def get(self,request,*args,**kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()#buscamos el toquen que coincida y si lo tenemos podemos tener el usuario de ese token


        if token:#validamos si existe el token
            user = token.user

            all_sessions = Session.objects.filter(expire_date__gte = datetime.now())#todas las sessiones que su tiempo de expiracion sea mayor igual que la hora actual
            if all_sessions.exists():
                for session in all_sessions:#busca en todas las sessiones aquella que corresponda con el usuario actual
                    session_data = session.get_decoded()
                    if user.id ==int(session_data.get("_auth_user_id")):#_auth_user_id es el id al cual corresponde la session,la igualamos con el id del usuario
                        session.delete() 
            #delete user tken
            token.delete()

            session_message = "Seciones de usuario eliminadas"
            token_message = "Token eliminado"
            return Response({"token_message":token_message,"session_message":session_message},status=status.HTTP_200_OK) 

        return Response({"error":"No se encontro un usuario con estas credenciales"},status=status.HTTP_400_BAD_REQUEST)
        
"""