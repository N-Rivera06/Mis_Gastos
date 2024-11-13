from rest_framework import serializers
from Users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
      class Meta:
        model = User
        fields= [ 'id','email','username', 'password' ]


       #override del método crear usuarios y que la contraseña se encripte y ojo debe ir alineado con UserRegisterSerializer
      def create(self, validated_data):
        password=validated_data.pop('password', None)
        instance= self.Meta.model(**validated_data)
        if password is not None:
                instance.set_password(password)
        instance.save()
        return instance


#Nuevo serializador para consultas

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields=['id','email','username', 'first_name', 'last_name']


#serializador para actualizar los datos de usuariao

class UserUpdateSerializer(serializers.ModelSerializer):
     class Meta:
          model= User
          fields=['first_name', 'last_name']