from rest_framework import serializers
from .models import Cliente, Reserva


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'documento']


class ReservaSerializer(serializers.ModelSerializer):
    # Campos personalizados del cliente
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    cliente_documento = serializers.CharField(source='cliente.documento', read_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id',
            'fecha_ingreso',
            'fecha_salida',
            'numero_habitacion',
            'cliente',             # Muestra el ID del cliente
            'cliente_nombre',      # Campo personalizado extra
            'cliente_documento'    # Campo personalizado extra
        ]
