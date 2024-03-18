from django.urls import reverse, resolve
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView

import os
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django.conf import settings

# Your tests go here
def test_example():
    assert 1 == 1 

def test_register_url():
    """Test register URL resolves to RegisterView."""
    url = reverse('rest_register')
    assert resolve(url).func.view_class == RegisterView

def test_login_url():
    """Test login URL resolves to LoginView."""
    url = reverse('rest_login')
    assert resolve(url).func.view_class == LoginView
    
