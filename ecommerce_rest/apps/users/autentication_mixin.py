from rest_framework.authentication import get_authorization_header
from rest_framework import status, authentication, exceptions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.users.autentication import ExpireTokenAutentication


class Authentication(authentication.BaseAuthentication):# para que la clase sea gloval en ves de heredar de "object"  lo hacemos de authentication.BaseAuthentication
    """
    Se hereda de BaseAuthentication porque este tiene el metodo autenticate()
    requerido para que la clase sea gloval,
    pero para que funcione tenemos que sobreescribir este metodo autenticate()
    devolviendo 2 valores en forma de tupla usuario y autentication
    lo estamos transformando a custom es decir no utilizamos el por defecto 
    sino que personalizamos las clases y metodos
    """
    
    
    user = None #usuario actual que realiza la peticion
    user_token_expired = False

    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()#la posicion [0] es "token" en el value del header
            except:    
                return None

            token_expire = ExpireTokenAutentication()
            user,token,message,self.user_token_expired = token_expire.authenticate_credentials(token)
            if user != None and token != None:
                self.user = user
                return user
            return message

        return None

    
    def authenticate(self,request):#request es un objeto de la class request de djando que reprecenta las peticiones
        self.get_user(request)#llamamos a get_user que es el que verifica la expiracion del token si pertenece al usuario y pone el valor en self.user
        if self.user is None:
            raise exceptions.AuthenticationFailed("Credenciales enviadas incorrectas")

        return(self.user, None)# este retorno ser va a request.user(va a estar la instacia) y request.auth(cualquier parametro que se nec para la autenticacion)
           
"""
Este ya no lo utilizamos porque no usamos mas el mixin ya que ahora la clase Autenticate es gloval

    def dispatch(self,request,*args,**kwargs):#dispatch es el primer metodo de cualquier clase django
        user = self.get_user(request)
        if user is not None:
            if type(user) == str:
                response = Response({"Error": user,"expired":self.user_token_expired},status=status.HTTP_401_UNAUTHORIZED)#si el usuario es un str quiere decir que es un mensje pq algo sucedio
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                return response

            return super().dispatch(request,*args,**kwargs)
        response =  Response({"error": "No se enviaron las credenciales..",
                              "expired":self.user_token_expired},status=status.HTTP_400_BAD_REQUEST)# de esta manera le avisamos al fronend cuando expiro el token
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response #hacemos todo esto para poder retornar las respuestas que establecimos

        """