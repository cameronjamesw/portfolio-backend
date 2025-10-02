from django.db import models
from django.conf import settings
from api.languages.models import Language

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    name = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    languages = models.ManyToManyField(
        Language,
        related_name="projects",
        null=True,
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

