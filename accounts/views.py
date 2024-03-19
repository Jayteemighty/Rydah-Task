from .models import User
from .serializers import UserSerializer
from dj_rest_auth.registration.views import RegisterView

class rest_register(RegisterView):
    queryset = User.objects.all()
    serializer_class = UserSerializer