from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    TipoEquipo, Fase, Estado, Kit, ArmadoKit, Equipo, Usuario,
    Movimiento, MovimientoKit, RegistroKey, RegistroDespliegue,
    Operador, Llave)

class TipoEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipo
        fields = '__all__'

class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fase
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = '__all__'

class ArmadoKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmadoKit
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'

class MovimientoKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoKit
        fields = '__all__'

class RegistroKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroKey
        fields = '__all__'

class RegistroDespliegueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDespliegue
        fields = '__all__'

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = '__all__'

class LlaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llave
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        if user.groups.exists():
            token['group'] = user.groups.first().name
        else:
            token['group'] = None
        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        # Add custom response data
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'groups': [group.name for group in user.groups.all()],
        }
        return data
