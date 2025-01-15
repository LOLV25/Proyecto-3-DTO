#Esto seria el controlador 

from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer, DTOEmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':  # Usar el DTO solo para la lista
            return DTOEmpleadoSerializer
        return EmpleadoSerializer  # Usar el serializer completo para crear/actualizar
