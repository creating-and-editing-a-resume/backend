from django.test import TestCase
from creating_and_editing_a_resume.user.models import (
    user.ResumeUser,
    about.Information,
    courses.Courses
    )
from core.enums import Limits, Regex


class ResumeUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = user.ResumeUser.objects.create(
            email = 'testuser@example.com',
            phone = '+79999999999',
            telegram = '@testuser',
            city = 'Город',
            birth_date = '2000-01-01'
        )

    def test_email(self):
        """Введённая почта совпадает с ожидаемой"""
        user = ResumeUserTest.user
        expected_email = user.email
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(expected_email, 'testuser@example.com')
        self.assertEqual(max_length, Limits.EMAIL_MAX_LEN.value)

    def test_phone(self):
        """Введённый номер телефона совпадает с ожидаемым"""
        user = ResumeUserTest.user
        expected_phone = user.phone
        help_text = user._meta.get_field('phone').help_text
        self.assertEqual(expected_phone, '+79999999999')
        self.assertEqual(help_text, 'Укажите номер телефона для связи')

    def test_telegram(self):
        """Введённый телеграм совпадает с ожидаемым"""
        user = ResumeUserTest.user
        expected_telegram = user.telegram
        help_text = user._meta.get_field('telegram').help_text
        self.assertEqual(expected_telegram, '@testuser')
        self.assertEqual(help_text, 'Аккаунт в Telegram. Начинается с @')

    def test_city(self):
        """Введённый город совпадает с ожидаемым"""
        user = ResumeUserTest.user
        expected_city = user.city
        help_text = user._meta.get_field('city').help_text
        max_length = user._meta.get_field('city').max_length
        verbose = user._meta.get_field('city').verbose_name
        self.assertEqual(expected_city, 'Город')
        self.assertEqual(help_text, 'Ваш город')
        self.assertEqual(max_length, Limits.USER_MODEL_MAX_LEN.value)
        self.assertEqual(verbose, 'Город')

    def test_birth_date(self):
        """Введённая дата рождения совпадает с ожидаемой"""
        user = ResumeUserTest.user
        expected_birth_date = user.birth_date
        help_text = user._meta.get_field('birth_date').help_text
        verbose = user._meta.get_field('birth_date').verbose_name
        self.assertEqual(expected_birth_date, '2000-01-01')
        self.assertEqual(help_text, 'Ваша дата рождения')
        self.assertEqual(verbose, 'Дата рождения')


class InformationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.about = about.Information.objects.create(
            user = about.Information.user.objects.create_user(username = 'testuser@example.com'),
            about = 'Я - тестовый юзер. Моё хобби - тесты.'
        )
    
    def test_about(self):
        """Введённая информация о себе совпадает с ожидаемой"""
        user = InformationTest.user
        expected_about = user.about
        help_text = user._meta.get_field('about').help_text
        self.assertEqual(expected_about, 'Я - тестовый юзер. Моё хобби - тесты.')
        self.assertEqual(help_text, 'Информация о себе, своих хобби и достижениях')


class CoursesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.courses = courses.Courses.objects.create(
            student = courses.Courses.user.objects.create_user(username = 'testuser@example.com'),
            company = 'Test Company',
            name = 'Test name',
            date = '2000-01-01',
            speciality = 'Test Speciality',
            experience = 'Test Experience',
            skills = 'Test Skills',
            diploma_link = 'https://testlink.com/test-diploma/'
        )

    def test_student(self):
        """Студент совпадает с ожидаемым"""
        courses = CoursesTest.courses
        expected_student = courses.student.username
        verbose = courses._meta.get_field('student').verbose_name
        self.assertEqual(expected_student, 'testuser@example.com')
        self.assertEqual(verbose, 'Студент курсов')

    def test_company(self):
        """Введённая организация совпадает с ожидаемой"""
        courses = CoursesTest.courses
        expected_company = courses.company
        help_text = courses._meta.get_field('company').help_text
        max_length = courses._meta.get_field('company').max_length
        self.assertEqual(expected_company, 'Test Company')
        self.assertEqual(help_text, 'Название организации проводившей обучение')
        self.assertEqual(max_length, Limits.USER_MODEL_MAX_LEN.value)
    
    def test_name(self):
        """Введённое название курса совпадает с ожидаемым"""
        courses = CoursesTest.courses
        expected_name = courses.name
        help_text = courses._meta.get_field('name').help_text
        max_length = courses._meta.get_field('name').max_length
        self.assertEqual(expected_name, 'Test Name')
        self.assertEqual(help_text, 'Название курса')
        self.assertEqual(max_length, Limits.USER_MODEL_MAX_LEN.value)

    def test_date(self):
        """Введённая дата окончания совпадает с ожидаемой"""
        courses = CoursesTest.courses
        expected_date = courses.date
        help_text = courses._meta.get_field('date').help_text
        self.assertEqual(expected_date, '2000-01-01')
        self.assertEqual(help_text, 'Дата окончания курсов')
        
    def test_experience(self):
        """Введённый опыт совпадает с ожидаемым"""
        courses = CoursesTest.courses
        expected_experience = courses.experience
        help_text = courses._meta.get_field('experience').help_text
        self.assertEqual(expected_experience, 'Test Experience')
        self.assertEqual(help_text, 'Полученный вами опыт')
        
    def test_skills(self):
        """Введённые навыки совпадают с ожидаемыми"""
        courses = CoursesTest.courses
        expected_skills = courses.skills
        help_text = courses._meta.get_field('skills').help_text
        self.assertEqual(expected_skills, 'Test Skills')
        self.assertEqual(help_text, 'Полученные вами навыки')
    
    def test_diploma_link(self):
        """Введённая ссылка совпадает с ожидаемой"""
        courses = CoursesTest.courses
        expected_diploma_link = courses.diploma_link
        help_text = courses._meta.get_field('diploma_link').help_text
        max_length = courses._meta.get_field('diploma_link').max_length
        self.assertEqual(expected_diploma_link, 'https://testlink.com/test-diploma/')
        self.assertEqual(help_text, 'Ссылка на проект/дипломную работу')
        self.assertEqual(max_length, Limits.URL_LEN.value)
    