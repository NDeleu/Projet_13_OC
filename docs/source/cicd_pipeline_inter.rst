Pipeline Interaction
====================

The CI/CD pipeline is a series of steps that our software application goes through
to make it into a user's hands. In the case of our application,
our CI/CD pipeline is orchestrated with GitLab CI/CD.
It starts when a developer pushes their changes into the Git repository.

The pipeline consists of the following stages:

1. **Build**: The build process involves a series of steps where the application is compiled. Environment variables are passed in from GitLab secrets.
2. **Lint Test**: The codebase is checked for any coding standards using flake8.
3. **Coverage Test**: This stage includes running unit tests and checking for code coverage. The target is to keep the coverage above 80%.
4. **Package**: The package stage builds the Docker image of the application and pushes it to DockerHub, Gitlab registry and AWS ECR.
5. **Deploy**: The deployment is the last stage where the application is deployed to AWS ECS.

This pipeline ensures a streamlined and consistent delivery of our software,
automated testing, and deployment, thereby improving productivity and efficiency.

The last two jobs are only allowed to the master branch.

