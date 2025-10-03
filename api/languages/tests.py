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

    def test_retrieve_languages(self):
        # Tests that languages can be retrieved by all users
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Ruby on Rails')

    def test_user_retrieve_languages(self):
        # Tests that languages can be retrieved by authenticated users
        self.client.login(username="user", password="password")

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Ruby on Rails')

    def test_admin_retrieve_languages(self):
        # Tests that languages can be retrieved by admin users
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

    def test_retrieve_language(self):
        # Tests that specific language can be retrieved by all users
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
        self.assertEqual(response.data['id'], self.language.pk)
    
    def test_user_retrieve_language(self):
        # Tests that specific language can be retrieved by authenticated users
        self.client.login(username="user", password="password")

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
        self.assertEqual(response.data['id'], self.language.pk)

    def test_admin_retrieve_language(self):
        # Tests that specific language can be retrieved by admin users
        self.client.login(username="admin", password="adminpassword")

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
        self.assertEqual(response.data['id'], self.language.pk)

    def test_unauthenticated_user_cannot_delete_language(self):
        # Tests that unauthenticated users cannot delete language
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())

    def test_user_cannot_delete_language(self):
        # Tests that authenticated users cannot delete language
        self.client.login(username="user", password="password")

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Language.objects.filter(pk=self.language.pk).exists())
    
    def test_admin_can_delete_language(self):
        # Tests that admin users can delete language
        self.client.login(username="admin", password="adminpassword")

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Language.objects.filter(pk=self.language.pk).exists())
