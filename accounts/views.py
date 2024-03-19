from dj_rest_auth.registration.views import RegisterView
from django.shortcuts import render

from .models import User
from .serializers import UserSerializer


class rest_register(RegisterView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def profile(request):
    return render(request, 'profile.html')
