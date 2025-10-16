from rest_framework import viewsets, filters
from .models import Cliente, Reserva
from .serializers import ClienteSerializer, ReservaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # Búsqueda por nombre o documento
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'documento']


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    # Búsqueda por número de habitación o nombre del cliente
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero_habitacion', 'cliente__nombre']
