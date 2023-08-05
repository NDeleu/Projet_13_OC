Deployment
==========

The deployment stage of the pipeline involves deploying the Dockerized application onto AWS ECS.

AWS ECS (Elastic Container Service) is a highly scalable, fast,
container management service that makes it easy to run, stop, and manage Docker containers on a cluster.
We have chosen AWS ECS due to its seamless integration with other AWS services, operational efficiency,
and the ability to easily scale our applications.

The ECS Cluster and Service are updated with the new Docker image in the deploy-job stage.
Task definitions are vital in ECS as they specify the Docker image to use for the container,
along with other parameters like port mappings, CPU, and memory considerations, etc.

To interact with AWS, the awscli is used, configured with secure keys for our AWS User.

Furthermore, to ensure high availability and fault tolerance, a Load Balancer has been configured.

This combination of AWS services ensures a robust and efficient production environment for our application.
