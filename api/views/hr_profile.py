from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from db.models import HRProfile
from api.serializers.hr_profile import HRProfileSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_hr_profile(request):
    if request.user.user_type != "HR":
        return Response(
            {"detail": "Only HR users can create HR profile"},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = HRProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    hr_profile, created = HRProfile.objects.update_or_create(
        user=request.user,
        defaults=serializer.validated_data
    )

    # mark onboarding as completed
    request.user.onboarding_completed = True
    request.user.save(update_fields=["onboarding_completed"])

    return Response(
        {
            "created": created,
            "profile": HRProfileSerializer(hr_profile).data
        },
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_hr_profile(request):
    if request.user.user_type != "HR":
        return Response(status=status.HTTP_403_FORBIDDEN)

    profile = getattr(request.user, "hr_profile", None)
    if not profile:
        return Response(
            {"detail": "HR profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(HRProfileSerializer(profile).data)
