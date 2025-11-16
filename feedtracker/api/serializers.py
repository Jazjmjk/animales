# api/serializers.py
from rest_framework import serializers

class RegistroSerializer(serializers.Serializer):
    porcentaje = serializers.FloatField()
    peso = serializers.FloatField()
    fecha = serializers.DateField()
    hora = serializers.TimeField()
