from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Framework
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class TestFrameworkDetailAPI(APITestCase):
    def setUp(self):
        # Set up pre-existing data for tests
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpassword")
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.framework = Framework.objects.create(
            owner = self.admin_user,
            name = "Django"
        )
        self.url = reverse('framework-list')

    def test_get_frameworks(self):
        # Tests GET method requests for each user class

        # Unauthenticated users
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Framework.objects.filter(pk=self.framework.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.framework.pk)
    
        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Framework.objects.filter(pk=self.framework.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.framework.pk)

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Framework.objects.filter(pk=self.framework.pk).exists())
        self.assertTrue(response.data['results'][0]['id'] == self.framework.pk)

    def test_only_admin_users_can_create_franework(self):
        # Tests POST method requests for each user class
        data = {
            'name': 'Laravel'
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
