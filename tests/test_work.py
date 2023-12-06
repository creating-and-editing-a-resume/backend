import pytest


class TestWork:

    @pytest.mark.django_db(transaction=True)
    def test_work_post(self, client, user):
        invalid_data = (
            'длииииииииииииииииииииииииииииииииииииииииииииииииииннннное '
            'назваааааааааааааааааааааааааааааааааааааааааааааааааааание '
        )
        invalid_data_company = {
            'company': invalid_data,
            'web_page': 'https://www.example.com/',
            'position': 'Должность',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'responsibilities': 'Мои обязанности и достижения',
        }
        response = client.post('/my-profile/', data=invalid_data_company)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `company`'
        )
        invalid_data_web_page = {
            'company': 'Название организации',
            'web_page': 'www.example',
            'position': 'Должность',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'responsibilities': 'Мои обязанности и достижения',
        }
        response = client.post('/my-profile/', data=invalid_data_web_page)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `web_page`'
        )
        invalid_data_position = {
            'company': 'Название организации',
            'web_page': 'https://www.example.com/',
            'position': invalid_data,
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'responsibilities': 'Мои обязанности и достижения',
        }
        response = client.post('/my-profile/', data=invalid_data_position)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `position`'
        )
        invalid_data_start_date = {
            'company': 'Название организации',
            'web_page': 'https://www.example.com/',
            'position': 'Должность',
            'start_date': '01.01.202',
            'end_date': '01.01.2022',
            'responsibilities': 'Мои обязанности и достижения',
        }
        response = client.post('/my-profile/', data=invalid_data_start_date)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `start_date`'
        )
        invalid_data_end_date = {
            'company': 'Название организации',
            'web_page': 'https://www.example.com/',
            'position': 'Должность',
            'start_date': '01.01.2021',
            'end_date': '01.01.202',
            'responsibilities': 'Мои обязанности и достижения',
        }
        response = client.post('/my-profile/', data=invalid_data_end_date)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `end_date`'
        )
        invalid_data_responsibilities = {
            'company': 'Название организации',
            'web_page': 'https://www.example.com/',
            'position': 'Должность',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'responsibilities': invalid_data,
        }
        response = client.post(
            '/my-profile/', data=invalid_data_responsibilities
        )
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `responsibilities`'
        )
        work_data = {
            'company': 'Название организации',
            'web_page': 'https://www.example.com/',
            'position': 'Должность',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'responsibilities': 'Мои обязанности и достижения',
        }
        response = client.post('/my-profile/', data=work_data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с корректными данными о работе возвращаете статус 201'
        )
        response_data = response.json()
        assert response_data.get('company') == work_data['company'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильное название организации'
        )
        assert response_data.get('web_page') == work_data['web_page'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильную ссылку на сайт организации'
        )
        assert response_data.get('position') == work_data['position'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильную должность'
        )
        assert response_data.get('start_date') == work_data['start_date'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильную дату начала работы'
        )
        assert response_data.get('end_date') == work_data['end_date'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильную дату окончания работы'
        )
        assert response_data.get(
            'responsibilities'
        ) == work_data['responsibilities'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильные данные об обязанностях и достижениях'
        )
    
    @pytest.mark.django_db(transaction=True)
    def test_work_patch(self, user):
        updated_work_data = {
            'company': 'Новое название организации',
            'web_page': 'https://www.new-example.com/',
            'position': 'Новая должность',
            'start_date': '01.02.2020',
            'end_date': '01.02.2021',
            'responsibilities': 'Новые обязанности и достижения',
        }
        response = user.client.patch('/my-profile/', data=updated_work_data)
        assert response.status_code == 200, (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными новыми данными о работе возвращаете статус 200'
        )
        response_data = response.json()
        assert response_data.get('company') == (
            updated_work_data['company'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'возвращаете правильное новое название организации'
            )
        )
        assert response_data.get('web_page') == (
            updated_work_data['web_page'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'возвращаете правильную новую ссылку на сайт организации'
            )
        )
        assert response_data.get('position') == (
            updated_work_data['position'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'возвращаете правильную новую должность'
            )
        )
        assert response_data.get('start_date') == (
            updated_work_data['start_date'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'возвращаете правильную новую дату начала работы'
            )
        )
        assert response_data.get('end_date') == (
            updated_work_data['end_date'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'возвращаете правильную новую дату окончания работы'
            )
        )
        assert response_data.get(
            'responsibilities'
        ) == updated_work_data['responsibilities'], (
            'Проверьте, что при PATCH запросе `/my-profile/` возвращаете '
            'правильные новые данные об обязанностях и достижениях'
        )
