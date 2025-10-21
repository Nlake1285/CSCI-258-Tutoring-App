from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    is_tutor = models.BooleanField(default=False, help_text="Is this user a tutor/TA?")
    classes_can_tutor = models.TextField(
        blank=True,
        help_text="Classes this TA can tutor (e.g., CSCI 150, CSCI 151)"
    )
    
    def __str__(self):
        return self.username