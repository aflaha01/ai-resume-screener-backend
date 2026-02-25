from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("HR", "HR"),
        ("JOB_SEEKER", "Job Seeker"),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        null=True,
        blank=True
    )

    onboarding_completed = models.BooleanField(default=False)
