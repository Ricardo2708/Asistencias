# Generated by Django 4.1.7 on 2023-06-10 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0015_remove_empleados_estado_empleado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado_datos',
            name='cargo',
            field=models.CharField(choices=[('MOZO RASTRA', 'MOZO RASTRA'), ('MOZO CAMION', 'MOZO CAMION'), ('OPERARIO', 'OPERARIO')], default='OPERARIO', max_length=100, verbose_name='Cargo:'),
        ),
        migrations.AlterField(
            model_name='empleado_datos',
            name='departamento',
            field=models.CharField(choices=[('RASTRA', 'RASTRA'), ('ADMINISTRACION', 'ADMINISTRACION'), ('PRODUCCION', 'PRODUCCION')], default='RASTRA', max_length=100, verbose_name='Departamento:'),
        ),
        migrations.AlterField(
            model_name='empleado_datos',
            name='dia_ingreso',
            field=models.CharField(default='10/06/23', max_length=100, verbose_name='Fecha De Ingreso:'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='estado',
            field=models.CharField(choices=[('SAB.', 'SAB.'), ('---', '---'), ('DESC', 'DESC'), ('X', 'X'), ('DOM.', 'DOM.'), ('VAC.', 'VAC.'), ('PCG', 'PCG'), ('PSG', 'PSG'), ('INC', 'INC')], max_length=100, verbose_name='Estado:'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='nombre_empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opcion1', to='asistencia.empleado_datos', verbose_name='Nombre:'),
        ),
    ]
