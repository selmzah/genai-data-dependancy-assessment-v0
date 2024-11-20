# Étape de construction
FROM node:16-alpine AS build

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Définir les arguments de build
ARG REACT_APP_API_URL

# Copier les fichiers package.json et package-lock.json dans le conteneur
COPY package*.json ./

# Installer les dépendances Node.js
RUN npm install

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

# Définir la variable d'environnement pour React
ENV REACT_APP_API_URL=${REACT_APP_API_URL}

# Construire l'application pour la production
RUN npm run build

# Étape de production
FROM node:16-alpine

# Installer un serveur HTTP léger pour servir l'application construite
RUN npm install -g serve

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers construits depuis l'étape de build
COPY --from=build /app/build ./build

# Exposer le port sur lequel l'application sera servie
EXPOSE 3000

# Ajouter un utilisateur non privilégié
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Définir la commande pour servir l'application
CMD ["serve", "-s", "build", "-l", "3000"]
