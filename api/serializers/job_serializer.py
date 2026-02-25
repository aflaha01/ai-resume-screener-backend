from rest_framework import serializers
from db.models.job import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "location",
            "job_type",
            "last_date",
            "status",
            "created_at",
        ]