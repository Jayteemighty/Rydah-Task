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
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("User registered successfully")
            return Response("User registered successfully", status=status.HTTP_201_CREATED)
        else:
            logger.error("User registration failed: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    API endpoint for user login.
    """
    
    def post(self, request):
        """
        Login an existing user.
        """
        logger.info("API POST request for user login")

        # Extract access token from request data
        access_token = request.data.get('access_token', None)
        if not access_token:
            logger.error("Access token is required")
            return Response("Access token is required", status=status.HTTP_400_BAD_REQUEST)

        # Get user information from Google using access token
        try:
            social_account = SocialAccount.objects.get(extra_data__contains={'access_token': access_token})
        except SocialAccount.DoesNotExist:
            logger.error("Invalid access token")
            return Response("Invalid access token", status=status.HTTP_400_BAD_REQUEST)

        # Get or create user based on Google account email
        try:
            user = User.objects.get(email=social_account.user.email)
        except User.DoesNotExist:
            user = User.objects.create_user(email=social_account.user.email)

        # You may customize this part to fetch more data from the social account if needed

        logger.info("User logged in successfully")
        return Response("User logged in successfully", status=status.HTTP_200_OK)
