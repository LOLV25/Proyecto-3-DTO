from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class DTOEmpleadoSerializer(serializers.ModelSerializer):
    # Concateno nombre y apellido
    Nombre_Completo = serializers.SerializerMethodField()

    class Meta:
        model = Empleado
        fields = ['cedula', 'Nombre_Completo', 'estado']

    def get_Nombre_Completo(self, obj):
        return f"{obj.nombre} {obj.apellido}"  
