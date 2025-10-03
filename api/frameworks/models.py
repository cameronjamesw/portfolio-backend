from django.db import models
from portfolio import settings

# Create your models here.

class Framework(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'frameworks'
    )
    name = models.CharField(
        max_length = 20,
        blank = False,
        unique = True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
