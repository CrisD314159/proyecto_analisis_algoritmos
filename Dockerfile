FROM python:3.9-slim

# Instalación de dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libffi-dev \
    libpq-dev \
    libjpeg-dev \
    libxml2-dev \
    libxslt1-dev \
    libz-dev \
    libgl1-mesa-glx \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instala pipenv
RUN pip install --no-cache-dir pipenv

# Establece directorio de trabajo
WORKDIR /app

# Copia solo Pipfile y Pipfile.lock primero (aprovecha cache)
COPY Pipfile Pipfile.lock /app/

# Instala las dependencias de pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copia el resto del proyecto
COPY . /app

# Expone el puerto para FastAPI
EXPOSE 8000

# Comando para ejecutar la app
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
