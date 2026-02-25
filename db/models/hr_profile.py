from django.conf import settings
from django.db import models

class HRProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="hr_profile"
    )
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="company_logos/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
