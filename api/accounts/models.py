from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(blank=False)
    profile_image = models.ImageField(upload_to="images/", 
                                      default="default_profile_pfhq2q",
                                      blank=True, null=True)

    def __str__(self):
        return self.username
