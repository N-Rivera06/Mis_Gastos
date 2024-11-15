# Generated by Django 5.1.2 on 2024-11-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProyeccionFinanciera',
            fields=[
                ('id_proyeccion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_proyeccion', models.DateField()),
                ('periodo_proyectado', models.CharField(choices=[('Semanal', 'Semanal'), ('Quincenal', 'Quincenal'), ('Mensual', 'Mensual'), ('Anual', 'Anual')], default='Mensual', max_length=10)),
                ('nombre_proyeccion', models.CharField(max_length=255)),
                ('informe', models.TextField(blank=True, db_collation='utf8mb4_general_ci', null=True)),
            ],
            options={
                'db_table': 'proyeccion_financiera',
                'managed': False,
            },
        ),
    ]
