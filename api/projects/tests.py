from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Project
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.
class TestProjectDetailAPI(APITestCase):
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
        # Tests that projects can be retrieved by unauthenticated users
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.project.name)

    def test_unauthorised_update_project(self):
        # Tests that unauthorised users cannot update projects
        data = {
            "name": "Test Project 2",
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorised_delete_project(self):
        # Tests that unauthorised users cannot delete projects
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_admin_can_delete_projects(self):
        # Tests that a normal user cannot delete projects
        self.client.login(username="user", password="password")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Tests that an admin user can delete projects
        self.client.login(username="admin", password="adminpassword")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestProjectAPI(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.normal_user = User.objects.create_user(username='user', password='password')
        self.url = reverse("project-list")

    def test_projects_retrieved(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.login(username="user", password="password")
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_project(self):
        data = {
            "name": "New Project",
            "description": "Desc",
            "live_link": "https://example.com",
            "repo_link": "https://github.com"
        }
    
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_only_admins_can_create_projects(self):
        data = {
            "name":  "Test Project",
            "description": "This is a test description",
            "image": "",
            "live_link": "https://heroku.com",
            "repo_link": "https://github.com",
        }
        
        self.client.login(username="user", password="password")
        request = self.client.post(self.url, data)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username="admin", password="adminpassword")
        request = self.client.post(self.url, data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
