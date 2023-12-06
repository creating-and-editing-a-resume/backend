import pytest


class TestAboutAPI:

    @pytest.mark.django_db(transaction=True)
    def test_about_me_post(self, user):
        about_data = {
            'about': 'Информация обо мне, моих хобби и достижениях'
        }
        response = client.post('/my-profile/', data=about_data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/my-profile/` '
            'с правильными данными возвращает 201.'
        )
    

    @pytest.mark.django_db(transaction=True)
    def test_about_me_patch(self, user):
        about_data = {
            'about': 'Новая информация обо мне, моих хобби и достижениях'
        }
        response = client.patch('/my-profile/', data=about_data)
        assert response.status_code == 200, (
            'Проверьте, что при PATCH запросе `/my-profile/` '
            'с правильными данными возвращает 200.'
        )
