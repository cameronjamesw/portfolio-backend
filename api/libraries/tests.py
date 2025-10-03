from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Library
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class TestLibraryListAPI(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpassword")
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.library = Library.objects.create(
            owner = self.admin_user,
            name = "React"
        )
        self.url = reverse('libraries-list')

    def test_retrieve_libraries(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.library.pk)
    
    def test_user_retrieve_libraries(self):
        self.client.login(username="user", password="password")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.library.pk)

    def test_admin_retrieve_libraries(self):
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Library.objects.filter(pk=self.library.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.library.pk)

    def test_unauthenticated_user_cannot_create_library(self):
        data = {
            'name': 'next.js'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_create_library(self):
        data = {
            'name': 'next.js'
        }
        self.client.login(username="user", password="password")
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_library(self):
        data = {
            'name': 'next.js'
        }
        self.client.login(username="admin", password="adminpassword")
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    