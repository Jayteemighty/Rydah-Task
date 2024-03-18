from django.urls import reverse, resolve
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from accounts.urls import urlpatterns as accounts_urls
import os
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django.conf import settings

# Your tests go here
def test_example():
    assert 1 == 1 

def test_admin_url():
    """Test admin URL resolves to admin site."""
    url = reverse('admin:index')
    assert resolve(url).func == admin.site.urls

def test_accounts_api_url():
    """Test accounts API URL resolves to accounts app's URLs."""
    url = reverse('accounts:rest_register')
    assert resolve(url).func.__name__ == 'RegisterView'

def test_api_schema_url():
    """Test API schema URL resolves to SpectacularAPIView."""
    url = reverse('schema')
    assert resolve(url).func.view_class == SpectacularAPIView

def test_api_docs_url():
    """Test API documentation URL resolves to SpectacularSwaggerView."""
    url = reverse('schema')
    assert resolve(url).func.view_class == SpectacularSwaggerView
