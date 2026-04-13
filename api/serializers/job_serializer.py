from rest_framework import serializers
from db.models.job import Job


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(
        source="created_by.hr_profile.company_name",
        read_only=True
    )

    match_percentage = serializers.IntegerField(read_only=True)

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "location",
            "job_type",
            "company_name",   
            "match_percentage",
            "last_date",
            "status",
            "created_at",
        ]