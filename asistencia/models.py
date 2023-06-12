from django.db import models
from datetime import datetime
from django.db import connection
from django.core.exceptions import ValidationError

ESTATUS ={
    ('EVENTUAL', 'EVENTUAL'),
    ('FIJO', 'FIJO')
}

ESTADOS = {
    ('X', 'X'),
    ('---', '---'),
    ('PSG', 'PSG'),
    ('PCG','PCG'),
    ('DESC', 'DESC'),
    ('INC','INC'),
    ('SAB.','SAB.'),
    ('DOM.','DOM.'),
    ('VAC.', 'VAC.')
}

DEPARTAMENTO ={
    ('RASTRA', 'RASTRA'),
    ('ADMINISTRACION', 'ADMINISTRACION'),
    ('PRODUCCION', 'PRODUCCION')
}

CARGO ={
    ('MOZO CAMION', 'MOZO CAMION'),
    ('MOZO RASTRA', 'MOZO RASTRA'),
    ('OPERARIO', 'OPERARIO')
}
today_empleado = datetime.today().strftime('%d/%m/%y')

class Empleado_datos(models.Model):
    numero_empleado = models.IntegerField(verbose_name='N° Empleado:')
    nombre_empleado_dato = models.CharField(max_length=100, verbose_name="Nombre:")
    dia_ingreso = models.CharField(max_length=100,verbose_name="Fecha De Ingreso:", default=today_empleado)
    departamento = models.CharField(max_length=100, verbose_name="Departamento:", choices=DEPARTAMENTO, default='RASTRA')
    cargo = models.CharField(max_length=100, verbose_name="Cargo:", choices=CARGO, default='OPERARIO')
    estatus = models.CharField(max_length=100, verbose_name="Estatus:", choices=ESTATUS, default='FIJO')
    honorario = models.CharField(max_length=100, verbose_name="Honorario: ",default="$ " )
    dui = models.CharField(max_length=10, verbose_name="Dui: ")
    telefono= models.CharField(max_length=10, verbose_name="Telefono:")
    cuenta_banco = models.CharField(max_length=20, verbose_name="Cuenta Banco: ")
    estado_empleado = models.BooleanField(verbose_name="Estado Empleado:", default=True)
    observación = models.TextField(verbose_name="Observación:", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Datos Empleados"
        verbose_name_plural = "Datos Empleados"

    def clean(self):
        self.nombre_empleado_dato = (self.nombre_empleado_dato).upper()  
        
    def __str__(self):
        return f'{self.nombre_empleado_dato}  | {self.cargo}'


class Empleados(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Empleado:', editable=False, default='')
    nombre_empleado = models.ForeignKey(Empleado_datos,verbose_name="Nombre:",on_delete=models.PROTECT, related_name='opcion1')
    estados = models.CharField(max_length=100, verbose_name="Estado:", choices=ESTADOS, default='FIJO')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')
    
    class Meta:
        verbose_name = "Estado Empleados"
        verbose_name_plural = "Estados Empleados"

    def clean(self):
        self.nombre = (self.nombre_empleado.nombre_empleado_dato).upper() 
        
    def __str__(self):
        return f' {self.nombre_empleado} | {self.estados}'
    

DIAS_EXTRAS={
    ('------', '-------'),
    ('DOMINGO', 'DOMINGO'),
    ('VACACION','VACACION')
}

today = datetime.today().strftime('%d/%m/%y')
today2 = datetime.today().strftime('%d')

class Asistencia(models.Model):
    titulo_asistencia = models.CharField(max_length=100, verbose_name='Titulo Registro:', default= f"DIA - {today2}", help_text=' --No Cambie el formato--' )
    empleado = models.ManyToManyField(Empleados, verbose_name="Empleado:",related_name='opcion1', default='')
    fecha = models.CharField(max_length=100, verbose_name='Fecha :', default=today)
    num_planilla = models.CharField(max_length=100, verbose_name="Planilla:", default='P', help_text='Numero De Planilla - Ejemplo:(P1)')
    comentarios = models.TextField(verbose_name="Comentarios:", blank=True, default=f"Asistencia Completada: {today}")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Asistencia 11 Al 25"
        verbose_name_plural = "Asistencias 11 - 25"

    def clean(self):
        self.titulo_asistencia = (self.titulo_asistencia).upper()
        self.num_planilla = (self.num_planilla).upper()

    def __str__(self):
        return f'{self.titulo_asistencia}'