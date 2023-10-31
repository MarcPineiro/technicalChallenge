# CI/CD Pipeline Workflow Explanation

This repository has a GitHub Actions CI/CD pipeline that automates the testing and deployment process for your application. The pipeline is divided into multiple stages, each with a specific purpose. This README.md file provides an explanation of each stage and how it contributes to the overall CI/CD process.

## 1. Build Stage

  - **Name:** build
  - **Triggers:** This stage is triggered on every push to the `main` branch.

  This stage sets up a MySQL database, installs necessary dependencies, migrates the database, and runs tests for your application to make sure the django code is correct. Here's a breakdown of the steps:

  1. **Checkout code:** This step checks out your code from the repository.

  2. **Setup Python:** It installs Python 3.10, which is the required Python version for your project.

  3. **Add hosts to /etc/hosts:** This step adds an entry to the system's hosts file to ensure the MySQL database can be accessed using a hostname.

  4. **apt update:** Updates the package list on the Ubuntu runner.

  5. **Install MySQL Server:** Installs the MySQL server.

  6. **Update setup MySQL SQL file:** It updates a SQL setup file with the values from GitHub Secrets.

  7. **Configure MySQL database:** This step configures the MySQL database with the provided credentials.

  8. **Install dependencies:** Installs Python dependencies from `requirements.txt`.

  9. **Migrate database:** Runs database migrations for your Django project.

  10. **Test code:** Runs the Django test suite for the `users` app.

## 2. Dockerize Stage

  - **Name:** dockerize
  - **Depends on:** build (this stage runs after the Django app is tested)

  This stage is responsible for building a Docker image of your application and saving it as an artifact to be used in kubernetes. Here are the steps:

  1. **Checkout code:** This step checks out your code.

  2. **Build image:** Builds a Docker image from your application code.

  3. **Save image:** Saves the Docker image as an artifact for later stages.

## 3. Deployment Stage

  - **Name:** deployment
  - **Depends on:** dockerize (this stage runs after the Docker image is built)

  The objective of this job is to create a minikube cluster to simulate the upload of an upgraded code to an existing cluster for production purposes. Here's how it works:

  1. **Checkout code:** This step checks out your code.

  2. **Start Minikube:** It starts a Minikube cluster.

  3. **Download Docker image:** Downloads the Docker image artifact created in the previous stage.

  4. **Load Docker image into Minikube:** Loads the Docker image into the Minikube environment.

  5. **Set environment values:** Modifies Kubernetes manifests to set environment variables and secrets based on GitHub Secrets.

  6. **Apply Kubernetes manifests:** Deploys the database and web application to the Kubernetes cluster.

  7. **Wait for services to be ready:** It waits for the database and web application to be ready.

  8. **Contact the Django app:** Tests the deployed application by making an HTTP request to an endpoint.

  9. **Error handling:** If there's an error in the HTTP request, it exits the workflow with an error code.

The minikube mysql pod created in the pipeline has not the volume because it creates an error with the runner since the data cannot be cleaned (minikube delete gives error in github actions) and the database doesn't gets initilized, making it not upgrade the changes and gives error if there is a difference between the data already saved and the configuration established in the github actions variables.

## Usage

1. Push to the main branch to trigger the full CI/CD pipeline.

## Variables

Ensure that you have the following variables set up in your GitHub repository:

- `DOCKER_IMAGE_NAME`
- `MYSQL_DATABASE`
- `MYSQL_DATABASE_HOST`
- `MYSQL_DATABASE_PORT`
- `REPLICA_NUMBER`
- `TEST_MYSQL_PASSWORD`
- `TEST_MYSQL_ROOT_PASSWORD`
- `TEST_MYSQL_USER`
- `TEST_SECRETS` 

This CI/CD pipeline automates the building and deployment of a Django application into a Minikube Kubernetes cluster. It's configured to adapt to the specified environment and handle error conditions in the deployment phase.