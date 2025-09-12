from django.db import models
from django.conf import settings
from languages.models import Language

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    name = models.CharField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    languages = models.ManyToManyField(
        Language,
        related_name="projects",
        )
    live_link = models.URLField(blank=False, null=False)
    repo_link = models.URLField(blank=False, null=False)
    thumbnail = models.ImageField(upload_to="projects", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} created at {self.created_at}'

