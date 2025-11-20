# ---- Imagen base ----
FROM python:3.13-slim

# ---- Evitar buffers en stdout/stderr ----
ENV PYTHONUNBUFFERED=1

# ---- Crear directorio de trabajo ----
WORKDIR /app

# ---- Instalar dependencias del sistema ----
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# ---- Copiar requerimientos ----
COPY feedtracker/requirements.txt /app/requirements.txt

# ---- Instalar dependencias de Python ----
RUN pip install --no-cache-dir -r /app/requirements.txt

# ---- Copiar todo el proyecto ----
COPY feedtracker /app

# ---- Exponer puerto para Django ----
EXPOSE 8000

# ---- Comando por defecto ----
CMD ["gunicorn", "feedtracker.wsgi:application", "--bind", "0.0.0.0:8000"]
