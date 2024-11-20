# Utiliser une image Python officielle comme image de base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y build-essential libffi-dev

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Définir les variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Ajouter un utilisateur non privilégié
RUN adduser --disabled-password appuser
USER appuser

# Définir la commande pour démarrer l'application
CMD ["flask", "run"]
