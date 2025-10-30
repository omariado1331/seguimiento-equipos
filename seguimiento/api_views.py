from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.serializers import ModelSerializer
from .models import (
    TipoEquipo, Fase, Estado, Kit, ArmadoKit, Equipo, Usuario,
    Movimiento, MovimientoKit, RegistroKey, RegistroDespliegue,
    Operador, Llave)

from .serializers import (
    TipoEquipoSerializer, FaseSerializer, EstadoSerializer,
    KitSerializer, ArmadoKitSerializer, EquipoSerializer,
    UsuarioSerializer, MovimientoSerializer, MovimientoKitSerializer,
    RegistroKeySerializer, RegistroDespliegueSerializer, OperadorSerializer, LlaveSerializer,
    CustomTokenObtainPairSerializer)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'groups']

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class TipoEquipoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer

class FaseViewSet(viewsets.ModelViewSet):
    queryset = Fase.objects.all()
    serializer_class = FaseSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class KitViewSet(viewsets.ModelViewSet):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer

class ArmadoKitViewSet(viewsets.ModelViewSet):
    queryset = ArmadoKit.objects.all()
    serializer_class = ArmadoKitSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

class MovimientoKitViewSet(viewsets.ModelViewSet):
    queryset = MovimientoKit.objects.all()
    serializer_class = MovimientoKitSerializer

class RegistroKeyViewSet(viewsets.ModelViewSet):
    queryset = RegistroKey.objects.all()
    serializer_class = RegistroKeySerializer

class RegistroDespliegueViewSet(viewsets.ModelViewSet):
    queryset = RegistroDespliegue.objects.all()
    serializer_class = RegistroDespliegueSerializer

class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

class LlaveViewSet(viewsets.ModelViewSet):
    queryset = Llave.objects.all()
    serializer_class = LlaveSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
