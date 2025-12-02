# ---- Imagen base ----
FROM python:3.13-slim

# ---- Evitar buffers en stdout/stderr ----
ENV PYTHONUNBUFFERED=1

# ---- Crear directorio de trabajo ----
WORKDIR /app

# ---- Instalar dependencias del sistema necesarias para MySQL ----
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# ---- Actualizar pip ----
RUN pip install --upgrade pip

# ---- Copiar requerimientos ----
COPY feedtracker/requirements.txt /app/requirements.txt

# ---- Instalar dependencias de Python ----
RUN pip install --no-cache-dir -r /app/requirements.txt

# ---- Copiar todo el proyecto ----
COPY feedtracker /app

# ---- Crear directorio para archivos estáticos ----
RUN mkdir -p /app/staticfiles

# ---- Recolectar archivos estáticos ----
RUN python manage.py collectstatic --noinput --clear

# ---- Exponer puerto (Railway usa PORT variable) ----
EXPOSE 8000

# ---- Comando por defecto ----
CMD gunicorn feedtracker.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 4 --timeout 120