# Generated by Django 4.1.7 on 2023-06-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0013_remove_asistencia_estado_empleados_estado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado_datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=100, verbose_name='Nombre:')),
                ('dia_ingreso', models.CharField(default='Ingreso: 10/06/23', max_length=100, verbose_name='Observación:')),
                ('departamento', models.CharField(choices=[('ADMINISTRACION', 'ADMINISTRACION'), ('PRODUCCION', 'PRODUCCION'), ('RASTRA', 'RASTRA')], default='RASTRA', max_length=100, verbose_name='Estatus:')),
                ('cargo', models.CharField(choices=[('MOZO CAMION', 'MOZO CAMION'), ('MOZO RASTRA', 'MOZO RASTRA'), ('OPERARIO', 'OPERARIO')], default='OPERARIO', max_length=100, verbose_name='Estatus:')),
                ('honorario', models.CharField(default='$ ', max_length=100, verbose_name='Honorario: ')),
                ('dui', models.CharField(max_length=10, verbose_name='Dui: ')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono:')),
                ('cuenta_banco', models.CharField(max_length=20, verbose_name='Cuenta Banco: ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado El :')),
            ],
            options={
                'verbose_name': 'Datos Empleados',
                'verbose_name_plural': 'Datos Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name': 'Empleados Items', 'verbose_name_plural': 'Empleados Items'},
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='comentarios',
            field=models.TextField(blank=True, default='Asistencia Completada: 10/06/23', verbose_name='Comentarios:'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fecha',
            field=models.CharField(default='10/06/23', max_length=100, verbose_name='Fecha :'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='titulo_asistencia',
            field=models.CharField(default='DIA - 10', help_text=' --No Cambie el formato--', max_length=100, verbose_name='Titulo Registro:'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='estado',
            field=models.CharField(choices=[('VAC.', 'VAC.'), ('---', '---'), ('X', 'X'), ('SAB.', 'SAB.'), ('PSG', 'PSG'), ('PCG', 'PCG'), ('DOM.', 'DOM.'), ('DESC', 'DESC'), ('INC', 'INC')], max_length=100, verbose_name='Estado:'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='estatus',
            field=models.CharField(choices=[('EVENTUAL', 'EVENTUAL'), ('FIJO', 'FIJO')], default='FIJO', max_length=100, verbose_name='Estatus:'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='observación',
            field=models.TextField(blank=True, default='Ingreso: 10/06/23', verbose_name='Observación:'),
        ),
    ]
