from django.conf import settings
import os
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django.conf import settings

# Your tests go here
def test_example():
    assert 1 == 1 
def test_secret_key():
    """Test SECRET_KEY is properly set."""
    assert settings.SECRET_KEY != ""

def test_database_settings():
    """Test database settings."""
    assert settings.DATABASES["default"]["ENGINE"] == "django.db.backends.postgresql_psycopg2"
    assert settings.DATABASES["default"]["NAME"] != ""
    assert settings.DATABASES["default"]["USER"] != ""
    assert settings.DATABASES["default"]["HOST"] != ""
    assert settings.DATABASES["default"]["PORT"] != ""

def test_rest_framework_authentication_classes():
    """Test REST framework authentication classes."""
    assert 'rest_framework.authentication.TokenAuthentication' in settings.REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"]

def test_google_oauth2_settings():
    """Test Google OAuth2 settings."""
    assert settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id'] != ""
    assert settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['secret'] != ""
    assert settings.SOCIALACCOUNT_PROVIDERS['google']['SCOPE'] == ['email', 'profile']
    assert settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['key'] == ''
    assert settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI != ""
