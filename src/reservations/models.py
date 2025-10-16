from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.documento}"


class Reserva(models.Model):
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    numero_habitacion = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.numero_habitacion} - {self.cliente.nombre}"
