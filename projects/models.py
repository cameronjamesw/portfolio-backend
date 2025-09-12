from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    name = models.CharField(blank=False)
    description = models.TextField()
    languages = models.CharField()
    live_link = models.CharField(blank=False)
    repo_link = models.CharField(blank=False)
    thumbnail = models.ImageField(upload_to="projects", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

