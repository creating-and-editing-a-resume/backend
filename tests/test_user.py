import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('user-list')
    data = {
        'email': 'test@example.com',
        'password': 'testpassword',
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['email'] == 'test@example.com'


@pytest.mark.django_db
def test_user_login(api_client, user):
    url = reverse('token_obtain_pair')
    data = {
        'email': user.email,
        'password': '1234567',
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_user_detail(api_client, user):
    url = reverse('user-detail', kwargs={'pk': user.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == user.email


@pytest.mark.django_db
def test_update_user(api_client, user):
    url = reverse('user-detail', kwargs={'pk': user.id})
    data = {
        'email': 'updated@example.com',
        'phone': '+79999999999',
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == 'updated@example.com'
    assert response.data['phone'] == '+79999999999'


@pytest.mark.django_db
def test_create_information(api_client, user):
    url = reverse('information-list')
    data = {
        'user': user.id,
        'about': 'Информация обо мне и о моих хобби.',
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['about'] == 'Информация обо мне и о моих хобби.'


@pytest.mark.django_db
def test_get_information(api_client, user, information):
    url = reverse('information-detail', kwargs={'pk': information.id})
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['about'] == information.about


@pytest.mark.django_db
def test_update_information(api_client, user, information):
    url = reverse('information-detail', kwargs={'pk': information.id})
    data = {
        'about': 'Обновлённая информация обо мне.',
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['about'] == 'Обновлённая информация обо мне.'

