Containerization
================

Containerization involves packaging an application along with its required environment.
It's a lightweight alternative to full machine virtualization.
The key benefits are consistency across development and production environments,
and distribution of applications that run reliably from one computing environment to another.

In our case, Docker is used for containerization.

The Dockerfile provided in the project root defines the steps to create a Docker image of the application.
It is based on Amazon Linux 2023, installs Python3 and pip, copies the application files into the container,
runs Django migrations, collects static files, and finally runs the server.

The .dockerignore file ensures that unnecessary files are not copied into the Docker image, keeping it lightweight.

The containerized application is then ready to be deployed anywhere without worrying about the environment setup.
