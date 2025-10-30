from django.db import models

# Create your models here.

class TipoEquipo(models.Model):
    TIPO_EQUIPO_CHOICES = [
        ('laptop', 'Laptop'),
        ('cpu', 'CPU'),
        ('monitor', 'Monitor'),
        ('impresora', 'Impresora'),
        ('mouse', 'Mouse'),
        ('teclado', 'Teclado'),
        ('audifonos', 'Audifonos'),
        ('otros', 'Otros'),
    ]
    nombre = models.CharField(
        max_length=50, 
        choices=TIPO_EQUIPO_CHOICES, 
        default='cpu')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.description}"

class Fase(models.Model):
    FASE_CHOICES = [
        ('recepcion', 'Recepcion'),
        ('custodio', 'Custodio'),
        ('revision', 'Revision'),
        ('clonacion', 'Clonacion'),
        ('masterizacion', 'Masterizacion'),
        ('entregado_a_ope', 'Entregado'),
        ('en_kit', 'Kit'),
        ('no_recibido', 'No Recibido'),
    ]
    nombre = models.CharField(
        max_length=50,
        choices=FASE_CHOICES,
        default='no_recibido',
        unique=True)

    def __str__(self):
        return self.nombre

class Llave(models.Model):
    codigo_equipo = models.CharField(max_length=100, unique=True)
    contador_cambio = models.IntegerField(default=0)
    contador_nuevo_registro = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.codigo_equipo}C{self.contador_cambio}R{self.contador_nuevo_registro}"

class Estado(models.Model):
    ESTADO_CHOICES = [
        ('defectuoso', 'Defectuoso'),
        ('contingencia', 'Contingencia'),
        ('reparacion', 'En Reparacion'),
        ('funcional', 'Funcional'),
        ('nuevo', 'Nuevo'),
    ]
    nombre = models.CharField(
        max_length=50,
        choices=ESTADO_CHOICES,
        default='funcional')
    description = models.TextField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.description}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

class Kit(models.Model):
    codigo = models.CharField(max_length=100)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.codigo

class Equipo(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, blank=True, null=True)
    llave = models.ForeignKey(Llave, on_delete=models.CASCADE, blank=True, null=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.serial_number

class ArmadoKit(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Kit: {self.kit.codigo} Equipo: {self.equipo.serial_number} - {self.tipo_equipo.nombre}"

class Coordinador(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    ruta = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Operador(models.Model):
    ESTADO_CHOICES = [
        ('postulante', 'Postulante'),
        ('seleccionado', 'Seleccionado'),
        ('contratado', 'Contratado'),
        ('sin_firmar_contrato', 'Sin Firmar Contrato'),
        ('renuncia', 'Renuncia'),
    ]

    nombre = models.CharField(max_length=100)
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE, blank=True, null=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(
        max_length=50, 
        choices=ESTADO_CHOICES,
        default='postulante',
        blank=True,
        null=True)

    def __str__(self):
        return self.nombre



class Movimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipo.serial_number} - {self.fase.nombre} - {self.fecha_movimiento}"

class MovimientoKit(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE, blank=True, null=True)
    fue_asignado_a_operador = models.BooleanField(default=False)
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.kit.codigo} - {self.fase.nombre} - {self.fecha_movimiento}"
#cambiar a reporte diario
class RegistroKey(models.Model):
    llave = models.ForeignKey(Llave, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    nro_estacion = models.CharField(max_length=100)
    registro_inicial = models.IntegerField(default=0) 
    registro_final = models.IntegerField(default=0)
    contaddor_cambios_inicial = models.IntegerField(default=0)
    contador_cambios_final = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    incidentes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Key: {self.llave} - Operador: {self.operador.nombre} - {self.fecha_registro} Llave Inicial: {self.nro_estacion}R{self.registro_inicial}C{self.contaddor_cambios_inicial} Llave Final: {self.nro_estacion}R{self.registro_final}C{self.contador_cambios_final}"

class RegistroDespliegue(models.Model):
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=100)
    fue_desplegado = models.BooleanField(default=False)
    llego_destino = models.BooleanField(default=False)
    incidentes = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Operador: {self.operador.nombre} - Llego a destino: {self.llego_destino} - {self.fecha_registro}"


