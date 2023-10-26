# API Server Documentation

## Table of Contents

1. [Local Setup](#local-setup)
2. [API Endpoints](#api-endpoints)
   - [Create a New User](#create-a-new-user)
   - [Retrieve User Information](#retrieve-user-information)
3. [Request/Response Format](#requestresponse-format)
   - [Create a New User](#create-a-new-user-request)
   - [Create a New User Response](#create-a-new-user-response)
   - [Retrieve User Information](#retrieve-user-information-request)
   - [Retrieve User Information Response](#retrieve-user-information-response)
   - [Error Response](#error-response)
4. [Error Codes](#error-codes)

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