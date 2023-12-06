import pytest


class TestProjects:

    @pytest.mark.django_db(transaction=True)
    def test_projects_post(self, client, user):
        invalid_data_name = {
            'name': (
                'длииииииииииииииииииииииииииииииииииииииииииннннное название',
            ),
            'info': 'Описание проекта',
            'web_page': 'https://www.example.com/my-project/'
        }
        response = client.post('/my-profile/', data=invalid_data_name)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `name`'
        )
        invalid_data_web_page = {
            'name': 'Название проекта',
            'info': 'Описание проекта',
            'web_page': 'www.example'
        }
        response = client.post('/my-profile/', data=invalid_data_web_page)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `web_page`'
        )
        projects_data = {
            'name': 'Название проекта',
            'info': 'Описание проекта',
            'web_page': 'https://www.example.com/my-project/'
        }
        response = client.post('/my-profile/', data=projects_data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с корректными данными о проектах возвращаете статус 201'
        )
        response_data = response.json()
        assert response_data.get('name') == projects_data['name'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильные данное название проекта'
        )
        assert response_data.get('info') == projects_data['info'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильное описание проекта'
        )
        assert response_data.get('web_page') == projects_data['web_page'], (
            'Проверьте, что при POST запросе `/my-profile/` возвращаете '
            'правильную ссылку на проект'
        )

    @pytest.mark.django_db(transaction=True)
    def test_projects_patch(self, user):
        updated_projects_data = {
            'name': 'Новое название проекта',
            'info': 'Новое описание проекта',
            'web_page': 'https://www.example.com/new-project/'
        }
        response = client.patch('/my-profile/', data=updated_projects_data)
        assert response.status_code == 200, (
            'Проверьте, что при PATCH запросе `/my-profile/`, '
            'пользователь может изменить данные о проектах'
            'и возвращаете статус 200'
        )
        response_data = response.json()
        assert response_data.get('name') == updated_projects_data['name'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'возвращаете правильное новое название проекта'
        )
        assert response_data.get('info') == updated_projects_data['info'], (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'возвращаете правильное новое описание проекта'
        )
        assert response_data.get('web_page') == (
            updated_projects_data['web_page'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'возвращаете правильную новую ссылку на проект'
            )
        )
