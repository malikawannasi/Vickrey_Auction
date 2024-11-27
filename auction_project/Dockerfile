# Utiliser l'image de base Python 3.10 slim
FROM python:3.10-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip
RUN pip install --upgrade pip

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Installer coverage pour le test de code et la génération de rapport HTML
RUN pip install coverage

# Copier le reste de l'application
COPY . .

# Exposer le port (exemple pour FastAPI/uvicorn)
EXPOSE 8000

# Commande pour démarrer l'application avec uvicorn
CMD ["uvicorn", "auction_project.asgi:application", "--host", "0.0.0.0", "--port", "8000"]



