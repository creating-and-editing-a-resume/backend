import pytest


class TestEducation:
    
    @pytest.mark.django_db(transaction=True)
    def test_education_post(self, auth_client, user):
        invalid_data = (
            'длииииииииииииииииииииииииииииииииииииииииииииннннное название'
        )
        invalid_data_university = {
            'university': invalid_data,
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'faculty': 'Факультет',
            'speciality': 'Специальность',
            'grade': 'Степень',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_university)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `university`'
        )
        invalid_data_start_date = {
            'university': 'Название университета',
            'start_date': '01.01.202',
            'end_date': '01.01.2022',
            'faculty': 'Факультет',
            'speciality': 'Специальность',
            'grade': 'Степень',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_start_date)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `start_date`'
        )
        invalid_data_end_date = {
            'university': 'Название университета',
            'start_date': '01.01.2021',
            'end_date': '01.01.202',
            'faculty': 'Факультет',
            'speciality': 'Специальность',
            'grade': 'Степень',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_end_date)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлены параметры ввода в поле `end_date`'
        )
        invalid_data_faculty = {
            'university': 'Название университета',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'faculty': invalid_data,
            'speciality': 'Специальность',
            'grade': 'Степень',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_faculty)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `faculty`'
        )
        invalid_data_speciality = {
            'university': 'Название университета',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'faculty': 'Факультет',
            'speciality': invalid_data,
            'grade': 'Степень',
        }
        response = auth_client.post('/my-profile/', data=invalid_data_speciality)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `speciality`'
        )
        invalid_data_grade = {
            'university': 'Название университета',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'faculty': 'Факультет',
            'speciality': 'Специальность',
            'grade': invalid_data,
        }
        response = auth_client.post('/my-profile/', data=invalid_data_grade)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'установлена максимальная длина поля `grade`'
        )
        education_data = {
            'university': 'Название университета',
            'start_date': '01.01.2021',
            'end_date': '01.01.2022',
            'faculty': 'Факультет',
            'speciality': 'Специальность',
            'grade': 'Степень',
        }
        response = auth_client.post('/my-profile/', data=education_data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/my-profile/` с '
            'валидными данными об образовании возвращается статус 201'
        )
        response_data = response.json()
        assert response_data.get('university') == (
            education_data['university'], (
                'Проверьте, что при POST запросе `/my-profile/` возвращаете '
                'правильные данные об университете'
            )
        )
        assert response_data.get('start_date') == (
            education_data['start_date'], (
                'Проверьте, что при POST запросе `/my-profile/` возвращаете '
                'правильные данные о дате начала обучения'
            )
        )
        assert response_data.get('end_date') == (
            education_data['end_date'], (
                'Проверьте, что при POST запросе `/my-profile/` возвращаете '
                'правильные данные о дате окончания обучения'
            )
        )
        assert response_data.get('faculty') == (
            education_data['faculty'], (
                'Проверьте, что при POST запросе `/my-profile/` возвращаете '
                'правильные данные о факультете'
            )
        )
        assert response_data.get('speciality') == (
            education_data['speciality'], (
                'Проверьте, что при POST запросе `/my-profile/` возвращаете '
                'правильные данные о специальности'
            )
        )
        assert response_data.get('grade') == (
            education_data['grade'], (
                'Проверьте, что при POST запросе `/my-profile/` возвращаете '
                'правильные данные о степени'
            )
        )

    @pytest.mark.django_db(transaction=True)
    def test_education_patch(self, user):
        updated_education_data = {
            'university': 'Новое название университета',
            'start_date': '01.02.2021',
            'end_date': '01.02.2022',
            'faculty': 'Новый факультет',
            'speciality': 'Новая специальность',
            'grade': 'Новая степень',
        }
        response = user.patch('/my-profile/', data=updated_education_data)
        assert response.status_code == 200, (
            'Проверьте, что при PATCH запросе `/my-profile/`, '
            'пользователь может изменить данные об образовании, '
            'и возвращается статус 200'
        )
        response_data = response.json()
        assert response_data.get('university') == (
            updated_education_data['university'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `university`'
            )
        )
        assert response_data.get('start_date') == (
            updated_education_data['start_date'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `start_date`'
            )
        )
        assert response_data.get('end_date') == (
            updated_education_data['end_date'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `end_date`'
            )
        )
        assert response_data.get('faculty') == (
            updated_education_data['faculty'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `faculty`'
            )
        )
        assert response_data.get('speciality') == (
            updated_education_data['speciality'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `speciality`'
            )
        )
        assert response_data.get('grade') == (
            updated_education_data['grade'], (
                'Проверьте, что при PATCH запросе `/my-profile/` '
                'с правильными данными возвращаете `grade`'
            )
        )
