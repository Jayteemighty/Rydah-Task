from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
import logging

User = get_user_model()

logger = logging.getLogger(__name__)

class RegisterAPIView(APIView):
    """
    API endpoint for user registration using Google OAuth.
    """
    def post(self, request):
        """
        Register a new user.
        """
        logger.info("API POST request for user registration")
        
        email = request.data.get('email', None)
        if not email:
            logger.error("Email is required")
            return Response("Email is required", status=status.HTTP_400_BAD_REQUEST)

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            logger.error("User already registered")
            return Response("User already registered", status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(email=email)

        logger.info("User registered successfully")
        return Response("User registered successfully", status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    """
    API endpoint for user login using Google OAuth.
    """
    def post(self, request):
        """
        Login an existing user.
        """
        logger.info("API POST request for user login")

        email = request.data.get('email', None)
        if not email:
            logger.error("Email is required")
            return Response("Email is required", status=status.HTTP_400_BAD_REQUEST)

        # Check if user exists in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.error("User not found")
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)

        logger.info("User logged in successfully")
        return Response("User logged in successfully", status=status.HTTP_200_OK)
