from rest_framework import serializers


class ProfileSaveSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(required=False, allow_blank=True)

    summary = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    skills = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    experience = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    education = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    projects = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    certifications = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
