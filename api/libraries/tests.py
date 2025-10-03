from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Library
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class TestLibraryListAPI(APITestCase):
    # Tests for libraries-list endpoint

    def setUp(self):
        # Set up pre-existing data for tests
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpassword")
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.library = Library.objects.create(
            owner = self.admin_user,
            name = "React"
        )
        self.url = reverse('libraries-list')

    def test_get_libraries(self):
        # Tests GET method requests for each user class

        # Unauthenticated users
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.library.pk)
    
        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.library.pk)

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.library.pk)

    def test_only_admin_users_can_create_library(self):
        # Tests POST method requests for each user class
        data = {
            'name': 'next.js'
        }

        # Unauthenticated users
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
class TestLibraryDetailAPI(APITestCase):
    # Tests for libraries-detail endpoint

    def setUp(self):
        # Set up pre-existing data for tests
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpassword")
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.library = Library.objects.create(
            owner = self.admin_user,
            name = "React"
        )
        self.url = reverse('libraries-detail', kwargs={"pk": self.library.pk})

    def test_get_library(self):
        # Tests GET method requests for each user class
        response = self.client.get(self.url)

        # Unauthenticated users
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['name'] == 'React')
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())

        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['name'] == 'React')
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['name'] == 'React')
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())

    def test_delete_library(self):
        # Tests DELETE method requests for each user class

        # Unauthenticated users
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())

        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Library.objects.filter(pk=self.library.pk).exists())

    def test_update_library(self):
        # Tests PUT method requests for each user class
        data = {
            "name": "next.js",
        }

        # Unauthenticated users
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
