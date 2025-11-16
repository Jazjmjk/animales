# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroSerializer
import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# Funciones para leer y guardar
def leer_datos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(DATA_FILE, "w") as f:
        json.dump(datos, f, indent=4)

# Listar y crear registros
class RegistroListCreate(APIView):
    def get(self, request):
        datos = leer_datos()

        # Filtrar por fecha si se pasa ?fecha=YYYY-MM-DD
        fecha = request.query_params.get("fecha")
        if fecha:
            datos = [r for r in datos if r["fecha"] == fecha]

        return Response(datos)

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            datos = leer_datos()
            datos.append(serializer.data)
            guardar_datos(datos)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detalles, actualizar y eliminar
class RegistroDetail(APIView):
    def get(self, request, index):
        datos = leer_datos()
        if 0 <= index < len(datos):
            return Response(datos[index])
        return Response({"error": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, index):
        datos = leer_datos()
        if 0 <= index < len(datos):
            serializer = RegistroSerializer(data=request.data)
            if serializer.is_valid():
                datos[index] = serializer.data
                guardar_datos(datos)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, index):
        datos = leer_datos()
        if 0 <= index < len(datos):
            eliminado = datos.pop(index)
            guardar_datos(datos)
            return Response(eliminado)
        return Response({"error": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

# Obtener el último registro
class RegistroUltimo(APIView):
    def get(self, request):
        datos = leer_datos()
        if datos:
            return Response(datos[-1])
        return Response({"error": "No hay registros"}, status=status.HTTP_404_NOT_FOUND)
