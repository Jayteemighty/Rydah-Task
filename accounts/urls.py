from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

urlpatterns = [
    #path('register/', views.RegisterAPIView.as_view()),
    #path('login/', views.LoginAPIView.as_view()),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
]