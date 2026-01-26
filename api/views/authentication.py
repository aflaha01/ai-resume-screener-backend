from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    User.objects.create_user(username=username, password=password)
    return Response({"message": "User registered successfully"})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {
                "message": "Username and password are required",
                "statusCode": 400
            },
            status=400
        )

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {
                "message": "Invalid username or password",
                "statusCode": 401
            },
            status=401
        )

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "statusCode": 200
        },
        status=200
    )

