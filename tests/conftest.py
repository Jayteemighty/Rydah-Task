import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from constants import EMAIL, PASSWORD, PASSWORD1, PASSWORD2


@pytest.fixture
def User():
    return get_user_model()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def signup_payload():
    return {EMAIL: 'test@gmail.com', PASSWORD1: 'pwdwrdss123', PASSWORD2: 'pwdwrdss123'}


@pytest.fixture
def signin_payload():
    return {
        EMAIL: 'test@gmail.com',
        PASSWORD: 'pwdwrdss123',
    }
