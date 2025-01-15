#Esto seria el DTO

from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'  # Todos los campos del modelo Empleado

class DTOEmpleadoSerializer(serializers.ModelSerializer):
    # Personalizamos los campos para que coincidan con los del DTO en C#
    Nombre_Completo = serializers.CharField(source='nombre', read_only=True)  # Tomamos 'nombre' y lo renombramos a 'Nombre_Completo'
    
    class Meta:
        model = Empleado
        fields = ['cedula', 'Nombre_Completo', 'estado']  # Solo los campos relevantes para la lista
