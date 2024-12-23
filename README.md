# Python Multi-Service Boilerplate

This project is a boilerplate for building Python microservices using Docker. It provides a structured way to manage multiple services that can share common modules.

## Project Structure

my_project/
├── shared_modules/
│ ├── init.py
│ ├── module1.py
│ └── module2.py
├── service_a/
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── service_b/
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── .env
├── .env.docker
└── docker-compose.yml

## Local Development

### Create Virtual Environment

To begin local development, it's recommended to create a virtual environment. This helps manage dependencies and avoid conflicts with system packages.

1. Navigate to the project root directory:

cd /path/to/my_project

2. Create a virtual environment

### Install Shared Modules

After activating your virtual environment, install the shared modules in editable mode:

pip install -e ./shared_modules

This command allows you to make changes to the shared modules without needing to reinstall them.

### Create `.env` File for Local Development

Create a `.env` file in the root directory of your project to define local environment variables. This file will be used by your services during development.

#### Example `.env` File

TEST="test text"

PYTHONPATH=/path/to/my_project

### Use Environment Variables

-   **Local Environment Variables**: Use the `.env` file for local development settings that your services will read at runtime.
-   **Docker Environment Variables**: Create a separate file named `.env.docker` for environment variables specifically used when running services in Docker. This helps keep your local and production configurations separate.

## Running Services with Docker

To run your services using Docker Compose, ensure you have Docker installed and running on your machine. Then, execute the following command from the project root:

docker-compose up --build

This command builds the images for each service and starts them up, allowing them to communicate with each other as defined in the `docker-compose.yml`.

## Conclusion

This boilerplate provides a solid foundation for developing Python microservices with shared modules. Customize it further according to your project's needs and enjoy building scalable applications!
