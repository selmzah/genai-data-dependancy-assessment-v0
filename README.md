# Data Dependency Assessment Project

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

This project aims to generate retro-documentation for Azure-based projects. It is an application that can generate documentation automatically according to a given template, using advanced language models.

- **Model**: GPT-4-32k
- **Embeddings**: Currently not implemented
- **Translation**: Not available yet

The main goal of this project is to provide an easy-to-use tool to help generate documentation for data dependencies in complex systems, particularly those utilizing Azure services.

### Built With

- **Python 3.10**
- **Flask** for backend API
- **React** for frontend development
- **Docker** for containerization
- **Neo4j** for graph database (optional integration)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To set up the project locally, follow these steps:

### Prerequisites

- Docker Desktop installed
- Access to the Azure Portal
- Python 3.10 installed on your machine

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/selmzah/genai-data-dependancy-assessment-v0.git
   ```

2. **Add Environment File**
   - Create a `.env` file at the root of the project based on the structure in `template.env`. This file should contain the necessary configuration for the project (e.g., database credentials, API keys).

3. **Build the Docker Image**
   - From the root directory of the project, run the following command to build a Docker image that includes both the backend and frontend:
   ```sh
   docker build -t data-dependency-assessment:latest -f backend/Dockerfile .
   ```

4. **Run the Docker Container**
   - Once the image is built, verify that it works correctly by running:
   ```sh
   docker run -p 5000:5000 --env-file .env data-dependency-assessment:latest
   ```
   - Access [http://localhost:5000](http://localhost:5000) in your browser to ensure that everything is running as expected.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dockerized Neo4j

To set up Neo4j using Docker, run the following command in PowerShell:

```sh
docker run -p 7474:7474 -p 7687:7687 --name neo4j-apoc --env='NEO4J_PLUGINS=["apoc"]' --env=NEO4J_AUTH=****/**** neo4j:latest
```

Replace `****/****` with your desired username and password for Neo4j.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

This application can be used to generate documentation automatically for various Azure-based projects. After setting up, simply navigate to the provided URL to use the application for generating documentation based on the input files and templates.

### Available Endpoints

- **GET /api**: Checks if the backend is running.
- **POST /api/explain_application**: Processes the input files and generates documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Add Embedding Capabilities
- [ ] Integrate Translation for Multi-Language Documentation
- [ ] Add Support for Other Databases
- [ ] Create More Flexible Documentation Templates

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star if you liked it!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Saad EL MZAH - saad.el-mzah@capgemini.com

Project Link: [https://github.com/selmzah/genai-data-dependancy-assessment-v0](https://github.com/selmzah/genai-data-dependancy-assessment-v0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [OpenAI GPT-4](https://openai.com/)
- [Neo4j](https://neo4j.com/)
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [React](https://reactjs.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

