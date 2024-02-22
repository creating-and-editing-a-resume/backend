import pytest


class TestCoursesAPI:

    @pytest.mark.django_db(transaction=True)
    def test_courses_post(self, auth_client, user):
        invalid_data = (
            'длииииииииииииииииииииииииииииииииииииииииииииииииииин '
            'ноооооооооооооооооооооооооооооооооооооооооооооооооооое '
            'назвааааааааааааааааааааааааааааааааааааааааааааааание '
        )
        invalid_data_company = {
            'company': invalid_data,
            'name': 'Название курса',
            'date': '01.01.2021',
            'speciality': 'Специальность',
            'experience': 'Полученный мной опыт',
            'skills': 'Полученные мной навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_company)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `company`'
        )
        invalid_data_name = {
            'company': 'Название организации',
            'name': invalid_data,
            'date': '01.01.2021',
            'speciality': 'Специальность',
            'experience': 'Полученный мной опыт',
            'skills': 'Полученные мной навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_name)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `name`'
        )
        invalid_data_date = {
            'company': 'Название организации',
            'name': 'Название курса',
            'date': '01.01.202',
            'speciality': 'Специальность',
            'experience': 'Полученный мной опыт',
            'skills': 'Полученные мной навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_date)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `date`'
        )
        invalid_data_speciality = {
            'company': 'Название организации',
            'name': 'Название курса',
            'date': '01.01.2021',
            'speciality': invalid_data,
            'experience': 'Полученный мной опыт',
            'skills': 'Полученные мной навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_speciality)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `speciality`'
        )
        invalid_data_experience = {
            'company': 'Название организации',
            'name': 'Название курса',
            'date': '01.01.2021',
            'speciality': 'Специальность',
            'experience': invalid_data,
            'skills': 'Полученные мной навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_experience)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `experience`'
        )
        invalid_data_skills = {
            'company': 'Название организации',
            'name': 'Название курса',
            'date': '01.01.2021',
            'speciality': 'Специальность',
            'experience': 'Полученный мной опыт',
            'skills': invalid_data,
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_skills)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `skills`'
        )
        invalid_data_diploma_link = {
            'company': 'Название организации',
            'name': 'Название курса',
            'date': '01.01.2021',
            'speciality': 'Специальность',
            'experience': 'Полученный мной опыт',
            'skills': 'Полученные мной навыки',
            'diploma_link': 'www.diploma-link'
        }
        response = auth_client.post('/my-profile/', data=invalid_data_diploma_link)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `diploma_link`'
        )
        courses_data = {
            'company': 'Название организации',
            'name': 'Название курса',
            'date': '01.01.2021',
            'speciality': 'Специальность',
            'experience': 'Полученный мной опыт',
            'skills': 'Полученные мной навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma/'
        }
        response = auth_client.post('/my-profile/', data=courses_data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращает 201.'
        )
        response_data = response.json()
        assert response_data.get('company') == courses_data['company'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `company`.'
        )
        assert response_data.get('name') == courses_data['name'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `name`.'
        )
        assert response_data.get('date') == courses_data['date'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `date`.'
        )
        assert response_data.get('speciality') == courses_data['speciality'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `speciality`.'
        )
        assert response_data.get('experience') == courses_data['experience'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `experience`.'
        )
        assert response_data.get('skills') == courses_data['skills'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `skills`.'
        )
        assert response_data.get('diploma_link') == courses_data['diploma_link'], (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращаете `diploma_link`.'
        )
    

    @pytest.mark.django_db(transaction=True)
    def test_courses_patch(self, user):
        updated_courses_data = {
            'company': 'Новое название организации',
            'name': 'Новое название курса',
            'date': '01.02.2021',
            'speciality': 'Новая специальность',
            'experience': 'Новый полученный опыт',
            'skills': 'Новые полученные  навыки',
            'diploma_link': 'https://www.diploma-link.com/my-diploma-1/'
        }
        response = user.patch('/my-profile/', data=updated_courses_data)
        assert response.status_code == 200, (
            'Проверьте, что при PATCH запросе `/my-profile/`, '
            'пользователь может изменить данные о курсах, и возвращается'
            ' статус 200'
        )
        response_data = response.json()
        assert response_data.get('company') == (
            updated_courses_data['company'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `company`.'
            )
        )
        assert response_data.get('name') == (
            updated_courses_data['name'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `name`.'
            )
        )
        assert response_data.get('date') == (
            updated_courses_data['date'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `date`.'
            )
        )
        assert response_data.get('speciality') == (
            updated_courses_data['speciality'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `speciality`.'
            )
        )
        assert response_data.get('experience') == (
            updated_courses_data['experience'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `experience`.'
            )
        )
        assert response_data.get('skills') == (
            updated_courses_data['skills'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `skills`.'
            )
        )
        assert response_data.get('diploma_link') == (
            updated_courses_data['diploma_link'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `diploma_link`.'
            )
        )
