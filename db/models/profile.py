# # db/models/profile.py
# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     resume = models.OneToOneField("Resume", on_delete=models.CASCADE)
    
#     name = models.CharField(max_length=255, blank=True)
#     email = models.EmailField(blank=True)
#     phone = models.CharField(max_length=20, blank=True)

#     summary = models.JSONField(default=list)
#     skills = models.JSONField(default=list)
#     education = models.JSONField(default=list)
#     experience = models.JSONField(default=list)
#     projects = models.JSONField(default=list)
#     certifications = models.JSONField(default=list)

#     created_at = models.DateTimeField(auto_now_add=True)
