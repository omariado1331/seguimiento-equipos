from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import CustomTokenObtainPairView

from .api_views import (TipoEquipoViewSet, FaseViewSet, EstadoViewSet,KitViewSet, ArmadoKitViewSet, EquipoViewSet,UsuarioViewSet, MovimientoViewSet, MovimientoKitViewSet,RegistroKeyViewSet, RegistroDespliegueViewSet,OperadorViewSet, LlaveViewSet, UserViewSet, GroupViewSet)

from . import views

router = routers.DefaultRouter()
router.register(r'tipo-equipos', TipoEquipoViewSet)
router.register(r'fases', FaseViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'kits', KitViewSet)
router.register(r'armado-kits', ArmadoKitViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'movimientos', MovimientoViewSet)
router.register(r'movimiento-kits', MovimientoKitViewSet)
router.register(r'registro-keys', RegistroKeyViewSet)
router.register(r'registro-despliegues', RegistroDespliegueViewSet)
router.register(r'operadores', OperadorViewSet)
router.register(r'llaves', LlaveViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

