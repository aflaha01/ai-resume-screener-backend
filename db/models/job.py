from django.db import models
from db.models.user import User


class Job(models.Model):
    JOB_STATUS_CHOICES = (
        ("active", "Active"),
        ("closed", "Closed"),
        ("draft", "Draft"),
    )

    JOB_TYPE_CHOICES = (
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
        ("Internship", "Internship"),
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)

    last_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=JOB_STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title