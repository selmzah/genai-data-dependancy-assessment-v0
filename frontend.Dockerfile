# Utilisez une image de base contenant Node.js
FROM node:14

# Copiez le package.json et le package-lock.json dans le conteneur
COPY frontend /app

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Installez les dépendances
RUN npm install

RUN npm build

# Exposez le port 80 pour que l'application puisse être accessible
EXPOSE 80

# Commande à exécuter lors du démarrage du conteneur
CMD ["npm", "start"]
