from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@api_view(['POST'])
def register(request):

    """
    Author: Aflaha on Jan 26, 2026
    Purpose: Registers a new user account.
    Input parameters: username, password
    Return: Returns success message or error message with status code
    """

    username = request.data.get('username')
    password = request.data.get('password')
    user_type = request.data.get('user_type')  

    if not username or not password or not user_type:
        return Response(
            {"error": "Username, password and user_type are required"},
            status=400
        )

    if user_type not in ["HR", "JOB_SEEKER"]:
        return Response(
            {"error": "Invalid user_type"},
            status=400
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "User already exists"},
            status=400
        )

    # Create user with role
    User.objects.create_user(
        username=username,
        password=password,
        user_type=user_type
    )

    return Response(
        {"message": "User registered successfully"},
        status=201
    )


@api_view(['POST'])
def login(request):
    
    """
    Author: Aflaha on Jan 26, 2026
    Purpose: Authenticates a user and returns JWT access and refresh tokens.
    Input parameters: username, password
    Return: Returns access token, refresh token, message, and status code
    """
    
    username = request.data.get('username')
    password = request.data.get('password')
    user_type = request.data.get('user_type') 

    if not username or not password or not user_type:
        return Response(
            {"message": "Username, password, and user_type are required"},
            status=400
        )

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {"message": "Invalid username or password"},
            status=401
        )

    if user.user_type != user_type:
        return Response(
            {"message": "You are not allowed to login as this role"},
            status=403
        )

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_type": user.user_type,
            "onboarding_completed": user.onboarding_completed
        },
        status=200
    )

