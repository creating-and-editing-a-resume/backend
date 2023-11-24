import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture
def password():
    return '1234567'


@pytest.fixture
def user(django_user_model, password):
    return django_user_model.objects.create_user(
        email='testuser@example.com',
        password=password
    )


@pytest.fixture
def unauth_client():
    client = APIClient
    return client


@pytest.fixture
def auth_client_1(unauth_client, user_1):
    unauth_client.force_authenticate(user=user_1)
    return unauth_client


@pytest.fixture
def invalid_token_client(unauth_client):
    unauth_client.credentials(HTTP_AUTHORIZATION='Token ' + 'invalid_token')
    return unauth_client
