from django.contrib import admin

# Register your models here.

from .models import (
    TipoEquipo,
    Fase,
    Estado,
    Kit,
    ArmadoKit,
    Equipo,
    Usuario,
    Movimiento,
    MovimientoKit,
    RegistroKey,
    RegistroDespliegue,
    Operador,
    Llave,
    Coordinador,
    Ruta,
)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'tipo_equipo', 'estado', 'usuario', 'modelo', 'marca')
    search_fields = ('serial_number', 'modelo', 'marca')
    list_filter = ('tipo_equipo', 'estado')

@admin.register(TipoEquipo)
class TipoEquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'description')
    search_fields = ('nombre',)

admin.site.register(Fase)
admin.site.register(Estado)
admin.site.register(Kit)
admin.site.register(ArmadoKit)
admin.site.register(Usuario)
admin.site.register(Movimiento)
admin.site.register(MovimientoKit)
admin.site.register(RegistroKey)
admin.site.register(RegistroDespliegue)
admin.site.register(Operador)
admin.site.register(Llave)
admin.site.register(Coordinador)
admin.site.register(Ruta)
