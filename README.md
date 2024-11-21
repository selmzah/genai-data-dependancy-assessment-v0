# Data Dependency (README TO UPDATE EVENTUALLY)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is an Azure project retro-documentation. 
It's an application which can generate documentation according to the giving template

Model: gpt-4-32k

Embeddings: No

Translation: No available for now

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

TODO

### Prerequisites
 
1. Have Docker Desktop installed
2. Have access to the Azure Portal
3. Have Python 3.10 installed

### Construire une image Docker pour le back-end avec le front-end inclus

1. Clone the project
   ```sh
   git clone https://github.com/selmzah/genai-data-dependancy-assessment-v0.git
   ```
2. Ajouter un fichier .env dans la racine du projet selon ce qui est indiqué dans template.env
3. Créer une image Docker unique : Depuis la racine du projet, exécutez la commande suivante :
   ```sh
   docker build -t data-dependency-assessment:latest -f backend/Dockerfile .
   ```
4. Vérifiez l'image : Une fois construite, vérifiez que l'image fonctionne correctement en la démarrant :
   ```sh
    docker run -p 5000:5000 --env-file .env data-dependency-assessment:latest
   ```
   Accédez à http://localhost:5000 pour valider que tout est fonctionnel.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dockerized NEO4J

To Dockerize Neo4j run this command in a PowerShell
    ```
    docker run -p 7474:7474 -p 7687:7687 --name neo4j-apoc --env='NEO4J_PLUGINS=[\"apoc\"]' --env=NEO4J_AUTH=****/**** neo4j:latest
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



