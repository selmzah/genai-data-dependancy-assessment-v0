# Étape 1 : Construire le front-end
FROM node:16 AS build-frontend
WORKDIR /app
COPY ./frontend ./
RUN npm install && npm run build

# Étape 2 : Préparer l'image Flask avec le front-end
FROM python:3.10
WORKDIR /app
COPY ./backend ./

# Copier tout le build du front-end directement dans le dossier /static
COPY --from=build-frontend /app/build/* ./static/

RUN pip install --no-cache-dir -r requirements.txt

# Commande pour démarrer Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
