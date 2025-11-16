# Dockerfile
FROM node:20-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY backend/package*.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el backend
COPY backend/ .

# Exponer puerto que usa tu app (ej: 3000)
EXPOSE 3000

# Comando para iniciar tu app
CMD ["node", "app.js"]

