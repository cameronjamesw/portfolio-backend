from django.db import models
from django.conf import settings

# Create your models here.

class Language(models.Model):
    name = models.CharField(blank=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="languages",
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
