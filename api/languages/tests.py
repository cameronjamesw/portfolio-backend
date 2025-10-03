from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Language
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class TestLangugagesListAPI(APITestCase):
    # Tests for language-list view

    def setUp(self):
        # Set up pre-existing data for tests
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpassword")
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.language = Language.objects.create(
            name = "Ruby on Rails"
        )
        self.url = reverse('language-list')

    def test_get_languages(self):
        # Tests GET method requests for each user class

        # Unauthenticated users
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Ruby on Rails')

        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Ruby on Rails')

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Ruby on Rails')


class TestLanguageDetailAPI(APITestCase):
    # Tests for the language-detail view

    def setUp(self):
        # Set up pre-existing data for tests
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpassword")
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.language = Language.objects.create(
            name = "Ruby on Rails"
        )
        self.url = reverse('language-detail', kwargs={'pk': self.language.pk})

    def test_get_language(self):
        # Tests GET method requests for each user class

        # Unauthenticated users
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
        self.assertEqual(response.data['id'], self.language.pk)
    
        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
        self.assertEqual(response.data['id'], self.language.pk)

        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
        self.assertEqual(response.data['id'], self.language.pk)

    def test_delete_language(self):
        # Tests DELETE method requests for each user class

        # Unauthenticated users
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())

        # Authenticated users
        self.client.login(username="user", password="password")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
    
        # Admin users
        self.client.login(username="admin", password="adminpassword")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Language.objects.filter(pk=self.language.pk).exists())
