from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from db.models.profile import UserProfile
from api.serializers.profile import ProfileSaveSerializer


class SaveProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        """
        Author: Aflaha on Feb 4, 2026
        Purpose: Saves or updates the authenticated user's profile data.
        Input parameters: profile data (JSON payload)
        Return: Returns saved profile data, created flag, message, and status code
        """

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

        return Response(
            {
                "message": "Profile saved successfully",
                "created": created,
                "profile": profile_obj.profile_json
            },
            status=status.HTTP_200_OK
        )
