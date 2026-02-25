from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from db.models.profile import UserProfile
from api.serializers.profile import ProfileSaveSerializer


class SaveProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProfileSaveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile_data = serializer.validated_data
        user = request.user

        profile_obj, created = UserProfile.objects.update_or_create(
            user=user,
            defaults={
                "profile_json": profile_data
            }
        )

        user.onboarding_completed = True
        user.save(update_fields=["onboarding_completed"])

        return Response(
            {
                "message": "Profile saved successfully",
                "onboarding_completed": True,
                "created": created,
                "profile": profile_obj.profile_json
            },
            status=status.HTTP_200_OK
        )


class GetSkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            profile_obj = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return Response(
                {"skills": []},
                status=status.HTTP_200_OK
            )

        skills = profile_obj.profile_json.get("skills", [])

        return Response(
            {"skills": skills},
            status=status.HTTP_200_OK
        )
