
# Create your models here.


# models.py

from django.db import models

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=13, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)
    usuario_creacion = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(null=True, blank=True)
    usuario_modificacion = models.IntegerField(null=True, blank=True)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'EMPLEADOS'
        indexes = [
            models.Index(fields=['cedula'], name='UQ__EMPLEADO__06BB84481363A4AA'),
        ]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


