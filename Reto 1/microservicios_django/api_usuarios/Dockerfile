# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Evita que Python escriba archivos pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Evita que Python almacene en búfer la salida stdout y stderr
ENV PYTHONUNBUFFERED=1

# Instala las dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copia los requirements e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el proyecto
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar las migraciones y el servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]