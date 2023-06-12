from django.contrib import admin
from .models import Empleado_datos,Empleados,Asistencia,Asistencia2
from import_export.admin import ImportExportModelAdmin


class Empleados_datosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('nombre_empleado_dato','dui','telefono' )
    list_filter=('created_at','departamento','cargo','estado_empleado')
    list_per_page = 20
    date_hierarchy= 'created_at'
    list_display=( 
        'nombre_empleado_dato',
        'numero_empleado',
        'departamento',
        'cargo',
        'estatus',
        'telefono',
        'estado_empleado'
    )


class EmpleadosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('nombre', )
    list_filter=('created_at','updated_at','estados', 'nombre')
    list_per_page = 20
    date_hierarchy= 'created_at'
    list_display=( 
        'nombre_empleado',
        'estados',
    )

class AsistenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('num_planilla', 'titulo_asistencia')
    list_filter=('created_at','updated_at','num_planilla')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'titulo_asistencia',
        'fecha',
        'num_planilla',
        'comentarios'
     )
    
class Asistencia2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('num_planilla2', 'titulo_asistencia2')
    list_filter=('created_at2','updated_at2','num_planilla2')
    list_per_page = 15
    date_hierarchy= 'created_at2'
    list_display=( 
        'titulo_asistencia2',
        'fecha2',
        'num_planilla2',
        'comentarios2'
     )



# Register your models here.
admin.site.register(Empleado_datos, Empleados_datosAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Asistencia2, Asistencia2Admin)

#Configuracion Del Panel
title = "Administracion"
subtitle = "Administracion"

admin.site.site_header =  title
admin.site.site_title = title
admin.site.index_title = subtitle