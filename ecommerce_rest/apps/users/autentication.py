from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

"""
Esto añade un tiempo de expiracion al token

"""

class ExpireTokenAutentication(TokenAuthentication):

    expired = False
    
    def expires_in(self,token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time #calcula el tiempo de expiracion
    
    
    def is_token_expired(self,token):
        return self.expires_in(token) < timedelta(seconds = 0) # nos dice si el token expiro
    
    def token_expire_handler(self,token):
        is_expired = self.is_token_expired(token)#is_token_expired realiza el calculo y aqui obtenemos el valor 
        
        if is_expired:
            self.expired = True
            user = token.user
            token.delete()#si expiro eliminamos el viejo toquen (si queremos sacarlo de la session lo ponemos aca)
            token = self.get_model().objects.create(user=user)#le creamos un nuevo token
        
        return is_expired, token

    def authenticate_credentials(self,key):
        message,token,user =  None,None,None
        try:
            token = self.get_model().objects.select_related("user").get(key = key)#get_model es un metodo de TokenAuthentication
            user = token.user       
        
        except self.get_model().DoesNotExist:
            message = "Token invalido"
            self.expired = True            
        
        if token is not None:
            if not token.user.is_active:
                message = "Usuario no activo o eliminado"
            
            is_expired = self.token_expire_handler(token)
        
       
            if is_expired:
                message = "Su token a expirado"
            
        return(user,token,message,self.expired)