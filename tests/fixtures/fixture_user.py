import pytest

from rest_framework.test import APIClient


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email = 'new_user@example.com',
        password = '1234567',
        first_name = 'Имя',
        last_name = 'Фамилия',
        phone = '+79999999999',
        telegram = '@telegram_username',
        city = 'Город',
        birth_date = '01.01.2000',
    )


@pytest.fixture
def unauth_client(user, resume):
    client = APIClient
    return client


@pytest.fixture
def auth_client(unauth_client, user):
    unauth_client.force_authenticate(user=user)
    return unauth_client


@pytest.fixture
def invalid_token_client(unauth_client):
    unauth_client.credentials(HTTP_AUTHORIZATION='Token ' + 'invalid_token')
    return unauth_client
