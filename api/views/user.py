from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from db.models import User
from api.serializers.user import UserMeSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserMeSerializer(request.user)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def complete_onboarding(request):
    """
    Purpose: Marks user onboarding as completed
    """
    user = request.user
    user.onboarding_completed = True
    user.save()

    return Response({
        "message": "Onboarding completed",
        "onboarding_completed": True
    })
