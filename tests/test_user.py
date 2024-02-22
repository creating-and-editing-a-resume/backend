import pytest
from django.contrib.auth import get_user_model


class TestUserAPI:

    @pytest.mark.django_db(transaction=True)
    def test_user_not_authenticated(self, unauth_client):
        response = unauth_client.get('/my-profile/')

        assert response.status_code != 404, (
            'Страница `/my-profile/` не найдена, проверьте этот адрес в '
            '*urls.py*'
        )

        assert response.status_code == 401, (
            'Проверьте, что при GET запросе `/my-profile/` без токена '
            'авторизации возвращается статус 401'
        )
    

    @pytest.mark.django_db(transaction=True)
    def test_user_post_guest(self, auth_client, user):
        empty_data = {}
        response = auth_client.post('/my-profile/', data=empty_data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с пустыми данными возвращаетe 400.'
        )
        no_email_data = {
            'password': '1234567'
        }
        response = auth_client.post('/my-profile/', data=no_email_data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` без email, '
            'возвращаетe статус 400.'
        )
        duplicate_email = {
            'email': user.email
        }
        response = auth_client.post('/my-profile/', data=duplicate_email)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с уже существующим email, возвращаете статус 400. '
            '`Email` должен быть уникальным у каждого прользователя.'
        )
        invalid_data_first_name = {
            'first_name': (
                'Имммммммммммммммммммммммммммммммммммммммммммммммммммммммммм '
                'ммммммммммммммммммммммммммммммммммммммммммммммммммммммммммя '
            ),
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': 'new_user@example.com'
        }
        response = auth_client.post(
            '/my-profile/', data=invalid_data_first_name
        )
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлена '
            'максимальная длина поля `first_name`'
        )
        invalid_data_last_name = {
            'first_name': 'Имя',
            'last_name': (
                'Фааааааааааааааааааааааааааааааамииииииииииииииииииииииииии '
                'лииииииииииииииииииииииииииииииииииииииииииииииииииииииииия '
            ),
            'password': '1234567',
            'email': 'new_user@example.com'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_last_name)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлена '
            'максимальная длина поля `last_name`'
        )
        invalid_data_email = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': (
                'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooo '
                'ooooooooooooooooooooooooooooooooooooooooooooong@example.com '
            )
        }
        response = auth_client.post('/my-profile/', data=invalid_data_email)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлена '
            'максимальная длина поля `email`'
        )
        invalid_data_phone = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': 'new_user@example.com',
            'phone': '1234567890123456789012'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_phone)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлены '
            'ограничения на длину поля `phone`'
        )
        invalid_data_telegram = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': 'new_user@example.com',
            'telegram': 'invalid_telegram_username_invalid_telegram_username',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_telegram)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлены '
            'ограничения на длину поля `telegram`'
        )
        invalid_data_birth_date = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': 'new_user@example.com',
            'birth_date': '0321521500',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_birth_date)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлены '
            'параметры ввода в поле `birth_date`'
        )
        invalid_data_city = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': 'new_user@example.com',
            'city': (
                'гоооооооооооооооооооооооооооооооооооооооооооооооооооооооо'
                'ооооооооооооооооооооооооооооооооооооооооооооооооооооооооо'
                'роооооооооооооооооооооооооооооооооооооооооооооооооооооооо'
                'оооооооооооооооооооооооооооооооооооооооооооооооооооооооод'
            ),
        }
        response = auth_client.post('/my-profile/', data=invalid_data_city)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` установлена '
            'максимальная длина поля `city`'
        )
        data = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': '1234567',
            'email': 'new_user@example.com',
            'phone': '+79999999999',
            'telegram': '@telegram_username',
            'birth_date': '01.01.2000',
            'city': 'Город'
        }
        response = auth_client.post('/my-profile/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращает 201.'
        )
        response_data = response.json()
        assert response_data.get('first_name') == data['first_name'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `first_name`.'
        )
        assert response_data.get('last_name') == data['last_name'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `last_name`.'
        )
        assert response_data.get('email') == data['email'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `email`.'
        )
        assert response_data.get('phone') == data['phone'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            ' с правильными данными возвращаете `phone`.'
        )
        assert response_data.get('telegram') == data['telegram'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `telegram`.'
        )
        assert response_data.get('birth_date') == data['birth_date'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `birth_date`.'
        )
        assert response_data.get('city') == data['city'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `city`.'
        )
        user = get_user_model()
        users = user.objects.all()
        assert get_user_model().objects.count() == users.count(), (
            'Проверьте, что при POST запросе `/my-profile/` вы создаёте '
            'пользователей.'
        )

    
    @pytest.mark.django_db(transaction=True)
    def test_user_patch_me(self, user):
        data = {
            'first_name': 'Новое имя',
            'last_name': 'Новая фамилия',
            'phone': '+79998888888',
            'telegram': '@new_telegram_username',
            'birth_date': '01.03.2000',
            'city': 'Новый город'
        }
        response = user.patch('/my-profile/', data=data)
        assert response.status_code == 200, (
            'Проверьте, что при PATCH запросе `/my-profile/`, '
            'пользователь может изменить свои личные данные, и возвращается'
            ' статус 200'
        )
        response_data = response.json()
        assert response_data.get('first_name') == data['first_name'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращаете `first_name`.'
        )
        assert response_data.get('last_name') == data['last_name'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращаете `last_name`.'
        )
        assert response_data.get('phone') == data['phone'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращаете `phone`.'
        )
        assert response_data.get('telegram') == data['telegram'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращаете `telegram`.'
        )
        assert response_data.get('birth_date') == data['birth_date'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращаете `birth_date`.'
        )
        assert response_data.get('city') == data['city'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращаете `city`.'
        )
