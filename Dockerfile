# Usamos una imagen base de Python 3.10-slim (compatible con TensorFlow y otras dependencias si las agregas)
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Actualiza pip e instala las dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que se ejecutará la aplicación (Render usa el puerto 10000 por defecto)
EXPOSE 10000

# Comando para iniciar la aplicación usando gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
