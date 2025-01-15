# Generated by Django 5.1.4 on 2025-01-14 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('sueldo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado', models.CharField(blank=True, max_length=1, null=True)),
                ('usuario_creacion', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
