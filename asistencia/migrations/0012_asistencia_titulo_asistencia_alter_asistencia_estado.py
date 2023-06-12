# Generated by Django 4.1.7 on 2023-06-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0011_remove_asistencia_empleado_alter_asistencia_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='titulo_asistencia',
            field=models.CharField(default='08 - ', max_length=100, verbose_name='Titulo Registro'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='estado',
            field=models.CharField(choices=[('PRESENTE', 'PRESENTE'), ('PSG', 'PSG'), ('AUSENTE', 'AUSENTE'), ('INC', 'INC'), ('DESC', 'DESC'), ('PCG', 'PCG')], max_length=100, verbose_name='Estado:'),
        ),
    ]
