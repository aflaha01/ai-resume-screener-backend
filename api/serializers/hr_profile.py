from rest_framework import serializers
from db.models import HRProfile

class HRProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRProfile
        fields = ["company_name", "industry", "logo"]
