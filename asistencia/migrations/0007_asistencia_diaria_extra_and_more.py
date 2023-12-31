# Generated by Django 4.1.7 on 2023-06-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0006_asistencia_diaria_fecha_final_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia_diaria',
            name='extra',
            field=models.CharField(choices=[('VACACION', 'VACACION'), ('DOMINGO', 'DOMINGO')], default=1, max_length=100, verbose_name='Extra:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asistencia_diaria',
            name='fecha_final',
            field=models.CharField(max_length=100, verbose_name='Fecha:'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='estados',
            field=models.CharField(choices=[('DESC', 'DESC'), ('PCG', 'PCG'), ('AUSENTE', 'AUSENTE'), ('PSG', 'PSG'), ('PRESENTE', 'PRESENTE'), ('INC', 'INC')], max_length=100, verbose_name='Estado:'),
        ),
    ]
