from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class CreateUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """
        Test creating a new user.
        """
        data = {
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpassword",
        }

        response = self.client.post('/api/users', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, "testuser@example.com")

    def test_create_user_invalid_data(self):
        """
        Test creating a new user with invalid data.
        """
        data = {}  # Invalid data, missing required fields
        response = self.client.post('/api/users', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
            password="testpassword"
        )

    def test_get_user(self):
        """
        Test retrieving user information.
        """
        user_id = self.user.id
        response = self.client.get(f'/api/users/{user_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], "testuser@example.com")
        self.assertEqual(response.data['first_name'], "Test")

    def test_get_user_not_found(self):
        """
        Test retrieving user information for a non-existent user.
        """
        invalid_user_id = 999  # Non-existent user
        response = self.client.get(f'/api/users/{invalid_user_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
