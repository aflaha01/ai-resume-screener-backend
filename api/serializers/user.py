from rest_framework import serializers
from db.models import User

class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "onboarding_completed"]
