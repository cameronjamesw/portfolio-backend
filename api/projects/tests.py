from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Project
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.
class TestProjectAPI(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.normal_user = User.objects.create_user(username='user', password='password') 
        self.project = Project.objects.create(
            user = self.admin_user,
            name = "Test Project",
            description = "This is a test description",
            image = "",
            live_link = "https://heroku.com",
            repo_link = "https://github.com",
        )

        self.url = reverse('project-detail', kwargs={'pk': self.project.pk})

    def test_get_project(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.project.name)

    def test_unauthorised_update_project(self):
        data = {
            "name": "Test Project 2",
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorised_delete_project(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_admin_can_delete_projects(self):
        self.client.login(username="user", password="password")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username="admin", password="adminpassword")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    