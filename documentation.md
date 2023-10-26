# API Server Documentation

## Table of Contents

1. [Local Setup](#local-setup)
2. [Docker Setup](#docker-setup)
3. [API Endpoints](#api-endpoints)
   - [Create a New User](#create-a-new-user)
   - [Retrieve User Information](#retrieve-user-information)
4. [Kubernetes Setup](#kubernetes-setup)
   - [Setting Up Minikube](#setting-up-minikube)
   - [Deploying the API Server](#deploying-the-api-server)
   - [Accessing the API Server](#accessing-the-api-server)
   - [Delete resources](#delete-resources)
5. [Request/Response Format](#requestresponse-format)
   - [Create a New User](#create-a-new-user-request)
   - [Create a New User Response](#create-a-new-user-response)
   - [Retrieve User Information](#retrieve-user-information-request)
   - [Retrieve User Information Response](#retrieve-user-information-response)
   - [Error Response](#error-response)
6. [Error Codes](#error-codes)

## Local Setup

To run the API server locally, follow these steps:

1. Clone the repository:
   ```
   git clone <https://github.com/MarcPineiro/technicalChallenge>
   ```

2. Navigate to the project directory:
   ```
   cd technicalChallenge
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations to set up the database:
   ```
   cd primaProject/
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

The API server will be accessible locally at [http://localhost:8000](http://localhost:8000).

## Docker Setup

Dockerizing your application allows you to create a portable and consistent environment for your Django app. This simplifies deployment and management, making it easier to scale, share, and maintain your application. Follow these steps to build and run the Docker container for your API server:

1. **Install Docker**: If you haven't already, install Docker on your machine by following the instructions for your specific platform: [Docker Installation Guide](https://docs.docker.com/get-docker/).

2. **Install Docker Compose**: If you haven't already, install Docker Compose on your machine by following the instructions for your specific platform: [Docker Compose Standalone Installation Guide](https://docs.docker.com/compose/install/standalone/).

3. **Run the Docker Container**:

   Start the Docker containers to start the Django application and the database to save all data:

   ```bash
   docker-compose up -d
   ```

   The `-d` flag indicates to start the services detached so you can use the terminal and have it runs on background.
   Its configurate to create a volume with the mySQL folder so the data is not lost between executions.

4. **Access the API**: Your Django application in the Docker container should be accessible at [http://localhost:8080](http://localhost:8080) on your host machine.

5. **Enter the containers**:

   If it's needed to execute anythin in the containers execute the command:
   ```bash
   docker container ls -a
   ```

   Copyt the id of the container you want to enter and use the command:
   ```bash
   docker exec -it <container_id> [sh/bash]
   ```

   For more information on the command read the [documentation](https://docs.docker.com/engine/reference/commandline/exec/)
   

## Kubernetes Setup

### Setting Up Minikube

1. **Install Minikube**: If you haven't already, install Minikube by following the official documentation: [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/).

2. **Start Minikube**: Start Minikube with the following command:

   ```bash
   minikube start
   ```

### Deploying the API Server

From now on we will use only kubectl for the commands of kubernetes, but working with minikube you can either substitute that for ```minikube kubectl -- ``` or create an alias of that by using ``` alias kubectl="minikube kubectl --" ```

1. **Apply Deployment and Service Manifests**:

   First create the image of the container for the aplication:
   
   ```bash
   eval $(minikube docker-env) #this is needed for minikube to actually see the image created
   docker build . -t imageName
   ```

   Once the image is build we will apply the files on the k8s folder so the API server gets deployed:

   ```bash
   cd ./k8s
   kubectl apply -f env-configmap.yaml
   kubectl apply -f db-claim0-persistentvolumeclaim.yaml
   kubectl apply -f djangonetwork-networkpolicy.yaml
   kubectl apply -f db-deployment.yaml
   kubectl apply -f db-service.yaml
   kubectl apply -f web-deployment.yaml
   kubectl apply -f web-service.yaml
   ```

   With this the enviroment for the API service will be deployed. (If the docuemts are updated the apply command will update the elements)

2. **Check Deployment Status**:

   Verify the deployment status using the following commands:

   ```bash
   kubectl get deployments
   kubectl get pods
   kubectl get services
   ```

   Ensure that the Deployment is running, Pods are in a ready state, and the Service is available.

### Accessing the API Server

To access your API server through the NodePort, follow these steps:

1. **Get the Server url**:

   Retrieve the Server url address using the following command:

   ```bash
   minikube service web --url
   ```

2. **Access the API Server**:

   With the resutl of the previous command we can start interacting with the server using the endpoints accessibles:

   ```bash
   curl http://MINIKUBE_IP:NODE_PORT/api/users/1
   curl -X POST http://MINIKUBE_IP:NODE_PORT/api/users -H 'Content-Type: application/json' -d '{"first_name": "John", "last_name": "Doe", "password": "securepassword", "email": "use3@example.com"}' 
   ```
   
### Delete resources

   To delete resources in minikube use the command:

   ```bash
   kubectl delete <resource-type> <name>
   ```

   If you don't know the name of the resource you can find it by using the command:

   ```bash
   kubectl get <resource-type> <name>
   ```

   Example:
   ```bash
   $> kubectl get service
      NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
      db           NodePort    10.98.155.120    <none>        3306:32292/TCP   72m
      kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          4h23m
      web          NodePort    10.106.191.136   <none>        8080:30008/TCP   72m
   $> kubectl delete service web
   ```

1. **Get the Server url**:

## Kubernetes for Deployment

Kubernetes is a container orchestration platform that provides numerous benefits for deploying and managing applications like yours:

- **Scalability**: Kubernetes allows you to easily scale your application by running multiple replicas, ensuring high availability and load balancing.

- **Resource Isolation**: Containers run in isolated environments, providing security and resource control.

- **Portability**: Applications are packaged as containers, making them highly portable and consistent across different environments.

- **Auto Healing**: Kubernetes automatically replaces failed containers or Pods, ensuring the application's reliability.

- **Rollouts and Rollbacks**: Kubernetes supports controlled updates and rollbacks, minimizing deployment risks.

- **Service Discovery and Load Balancing**: Kubernetes provides built-in service discovery and load balancing for your application's services.

By using Kubernetes, you enhance the scalability, availability, and manageability of your application, making it suitable for deployment in production environments.

## API Endpoints

### Create a New User

- **URL:** `/api/users`
- **HTTP Method:** POST
- **Description:** Create a new user by providing user details in the request body.

### Retrieve User Information

- **URL:** `/api/users/{user_id}`
- **HTTP Method:** GET
- **Description:** Retrieve user information by user ID.

## Request/Response Format

### Create a New User (POST /api/users)

**Request:**

```json
{
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "securepassword"
}
```

**Response (Success):**

```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_active": true,
  "is_staff": false,
  "date_joined": "2023-10-26T12:34:56.789012Z"
}
```

**Response (Error):**

In case of an error, the response will include an error message with an appropriate status code.

**Curl command example:**

```
curl -X POST http://127.0.0.1:8000/api/users -H 'Content-Type: application/json' -d '{"first_name": "John", "last_name": "Doe", "password": "securepassword", "email": "use3@example.com"}'
```

### Retrieve User Information (GET /api/users/{user_id})

**Response (Success):**

```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_active": true,
  "is_staff": false,
  "date_joined": "2023-10-26T12:34:56.789012Z"
}
```

**Response (Error):**

In case the user is not found, the response will include a 404 Not Found status.

### Error Response

In case of an error, the response will include an error message with an appropriate status code.

**Curl command example:**

```
curl -X POST http://127.0.0.1:8000/api/users -H 'Content-Type: application/json' -d '{"first_name": "John", "last_name": "Doe", "password": "securepassword", "email": "use3@example.com"}'
```

## Error Codes

- 400 Bad Request: When the request data is invalid or missing required fields.
- 404 Not Found: When the requested user does not exist.
- 500 Internal Server Error: For other unexpected server errors.