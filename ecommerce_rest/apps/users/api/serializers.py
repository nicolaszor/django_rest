from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email","name","last_name")


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):#utilizamos model para indicarle que va a estar basado en un modelo
    class Meta:
        model = User
        fields = "__all__"

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        return user
    def update(self,instance,validated_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validated_data["password"])
        update_user.save()
        return update_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    #mostrar solo campos que queramos mientras los guardamos con  el resto 
    def to_representation(self,instance):
        #data = super().to_representation(instance)#lo que hace es llamar a los campos en field y coloca clave valor con la consulta
        return {
            "id" : instance["id"],
            "username": instance["username"],
            "email" : instance["email"],
            "password": instance["password"],
        }




"""
class TestUserSerializer(serializers.Serializer):
    
        Para un serializador existen todos los mismos campos
        que para un modelo (Charfield,Emailfield,Booleanfield,etc...)
        primero se fija si hay una funcion def validate_"campo"() despues activa 
        automaticamente el metodo def validate(self,data)
  
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField(max_length = 200)

    def validate_name(self,value):
        #validation custom
        if value == "develop":
            raise serializers.ValidationError("Error, no puede existir un usuario con ese nombre")#utilizamos raise apra que l ometa dentro de errors
        print(value)
        return value
    
    def validate_email(self,value):
        print(value)
        return value
        if self.validate_name(self.context["name"]) in value:#self.context refiere a TestUserSerializer(context =test_data) en api.py
            raise serializers.ValidationError("el email no puede contener el nombre")
            #lo mismo que con validate de abajo pero de otra manea utilizando el contexto de api.

    
    def validate(self,data):
        if data["name"] in data["email"]:
            raise serializers.ValidationError("el email no puede contener el nombre")
        print("validate general")
        return data
    
    def create(self,validated_data):#validate_data es la informacion valida que ya paso por is_valid()
        print(validated_data)#para que este print funcione en las vistas tenemos que llamar a .save()
        return User.objects.create(**validated_data)#neceistamos un objeto o instancia en este caso utilizamos el modelo User
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)#esto lo va a hacer con cada campo que tenga definido el serializador email, name etc
        instance.email = validated_data.get("email",instance.email)
        instance.save()#todo esto es lo que hace automaticamente, este save()reprecenta a la instancia que es una clase de un MOdelo
        return instance


Podemos sobreescribir el metodo save() con un def save(self) y el metodo en vez de guardar en la
db va a hacer lo que le digamos.
esto nos puede servir para realizar validaciones pero no registros en la DB
eg. enviar al email en vez de guardar

def save(self):
    print(self.validated_data)
    send_email()
"""
