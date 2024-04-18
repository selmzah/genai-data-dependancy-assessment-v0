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

### Installation without docker (front/back)

1. Clone the project
   ```sh
   git clone https://gitlab.lafabric.ovh/gen-ai/data-dependency.git
   ```
2. Set OPEN API keys in .env file (Available on the Azure Portal)
   ```sh
   OPENAI_API_BASE=<url>
   OPENAI_API_KEY=<token>
   LOGIN_NEO4J=<login>
   PASSWORD_NEO4J=<password>
   ```
3. Create two terminals :
   * FRONTEND
   * BACKEND

#### To Launch FRONTEND:

1. Install all the dependencies
   ```sh
   cd frontend
   npm install --force
   ```
2. Start frontend
   ```sh
   npm start
   ```

#### To Launch BACKEND

1. Create a virtual env
   ```
   python -m venv .venv
   ```

2. Install all the dependencies
   ```sh
   cd backend
   pip install -r requirement.txt
   ```
3. Start backend
   ```sh
   flask run
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dockerized NEO4J

To Dockerize Neo4j run this command in a PowerShell
    ```
    docker run -p 7474:7474 -p 7687:7687 --name neo4j-apoc --env='NEO4J_PLUGINS=[\"apoc\"]' --env=NEO4J_AUTH=****/**** neo4j:latest
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



