# Generated by Django 4.1.7 on 2023-06-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0017_rename_nombre_empleado_empleado_datos_nombre_empleado_dato_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='estatus',
        ),
        migrations.AddField(
            model_name='empleado_datos',
            name='estatus',
            field=models.CharField(choices=[('EVENTUAL', 'EVENTUAL'), ('FIJO', 'FIJO')], default='FIJO', max_length=100, verbose_name='Estatus:'),
        ),
        migrations.AddField(
            model_name='empleados',
            name='estados',
            field=models.CharField(choices=[('DOM.', 'DOM.'), ('SAB.', 'SAB.'), ('PSG', 'PSG'), ('PCG', 'PCG'), ('INC', 'INC'), ('X', 'X'), ('DESC', 'DESC'), ('---', '---'), ('VAC.', 'VAC.')], default='FIJO', max_length=100, verbose_name='Estatus:'),
        ),
        migrations.AlterField(
            model_name='empleado_datos',
            name='cargo',
            field=models.CharField(choices=[('MOZO RASTRA', 'MOZO RASTRA'), ('MOZO CAMION', 'MOZO CAMION'), ('OPERARIO', 'OPERARIO')], default='OPERARIO', max_length=100, verbose_name='Cargo:'),
        ),
        migrations.AlterField(
            model_name='empleado_datos',
            name='departamento',
            field=models.CharField(choices=[('ADMINISTRACION', 'ADMINISTRACION'), ('RASTRA', 'RASTRA'), ('PRODUCCION', 'PRODUCCION')], default='RASTRA', max_length=100, verbose_name='Departamento:'),
        ),
    ]
