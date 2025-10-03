from django.db import models
from django.conf import settings
from api.languages.models import Language
from api.frameworks.models import Framework
from api.libraries.models import Library

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    name = models.CharField(blank=True, null=True)
    collaboration = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    languages = models.ManyToManyField(
        Language,
        related_name="projects",
        blank=True
        )
    libraries = models.ManyToManyField(
        Library,
        related_name="projects",
        blank=True
    )
    frameworks = models.ManyToManyField(
        Framework,
        related_name="projects",
        blank=True
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_image_nyj9lt',
        blank=True)
    live_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} created at {self.created_at}'

