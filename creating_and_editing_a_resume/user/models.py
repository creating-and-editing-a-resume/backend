from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


from .service import validate_starts_with
from creating_and_editing_a_resume.settings import (
    USER_MODEL_MAX_LEN,
    EMAIL_MAX_LEN,
    GRADE,
    )


class ResumeUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        null=False,
        unique=True,
        max_length=EMAIL_MAX_LEN
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Пароль необходим!',
    )
    first_name = models.CharField(
        verbose_name='Имя',
        null=True,
        blank=True,
        max_length=USER_MODEL_MAX_LEN,
        help_text='Имя пользователя',
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        verbose_name='Фамилия',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Фамилия пользователя',
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        null=True,
        blank=True,
        max_length=USER_MODEL_MAX_LEN,
        help_text='Номер телефона',
    )
    telegram = models.CharField(
        verbose_name='Telegram',
        null=True,
        blank=True,
        max_length=33,
        help_text='Аккаунт в Telegram. Начинается с @',
        validators=[
            MinLengthValidator(
                6,
                message='Длинна аккаунта в Tg минимум 5 символов.',
            ),
            validate_starts_with,
        ]
    )
    city = models.CharField(
        verbose_name='Город',
        null=True,
        blank=True,
        max_length=USER_MODEL_MAX_LEN,
        help_text='Ваш город',
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        help_text='Ваша дата рождения',
        null=True,
        blank=True,
    )
    username_field = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'Пользователь {self.email}'


User = ResumeUser


class EmploymentHistory(models.Model):
    employee = models.ForeignKey(
        ResumeUser,
        verbose_name='Работник',
        on_delete=models.CASCADE,
        db_index=True,
    )
    company = models.CharField(
        verbose_name='Организация',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Название организации',
    )
    web_page = models.CharField(
        verbose_name='Сайт',
        null=True,
        blank=True,
        help_text='Сайт организации',
    )
    position = models.CharField(
        verbose_name='Должность',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Ваша должность в компании',
    )
    start_date = models.DateField(
        verbose_name='Дата начала работы',
        help_text='Дата начала работы',
    )
    end_date = models.DateField(
        default=timezone.now(),
        null=True,
        blank=True,  # Если пусто - по настоящее время
        verbose_name='Дата окончания работы',
        help_text='Дата окончания работы',
    )
    responsibilities = models.TextField(
        verbose_name='Ваши обязанности и достижения',
        help_text='Перечислите ваши обязанности и достижения',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'employee',
                    'company',
                    'position'
                    ],
                name='unique_work_in_one_company'),
        ]
        default_related_name = 'works'
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'
        ordering = ('company',)

    def __str__(self):
        return (f'{self.employee.first_name} {self.employee.last_name}'
                f'работал в "{self.company}"')


class Courses(models.Model):
    student = models.ForeignKey(
        ResumeUser,
        verbose_name='Студент курсов',
        on_delete=models.CASCADE,
        db_index=True,
    )
    company = models.CharField(
        verbose_name='Организация',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Название организации проводившей обучение',
    )
    name = models.TextField(
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Название курса',
        help_text='Название курса',
    )
    date = models.DateField(
        verbose_name='Дата окончания курсов',
        help_text='Дата окончания курсов',
    )
    speciality = models.CharField(
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Специальность',
        help_text='Ваша специальность',
    )
    experience = models.TextField(
        verbose_name='Опыт',
        help_text='Полученный вами опыт',
    )
    skills = models.TextField(
        verbose_name='Навыки',
        help_text='Полученные вами навыки',
    )
    diplom_link = models.CharField(
        null=True,
        blank=True,
        verbose_name='Ссылка на проект/дипломную работу',
        help_text='Ссылка на проект/дипломную работу',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'student',
                    'company',
                    'name',
                    'date'
                    ],
                name='unique_course_in_one_time'),
        ]
        default_related_name = 'courses'
        verbose_name = 'Повышение квалификации'
        verbose_name_plural = 'Повышение квалификации'
        ordering = ('company', )

    def __str__(self):
        return (f'{self.student.first_name} {self.student.last_name}'
                f' повышал квалификацю "{self.name}" в "{self.company}"')


class Education(models.Model):
    student = models.ForeignKey(
        ResumeUser,
        verbose_name='Студент',
        on_delete=models.CASCADE,
        db_index=True,
    )
    university = models.CharField(
        verbose_name='ВУЗ',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Название учебного заведения',
    )
    start_date = models.DateField(
        verbose_name='Дата поступления',
        help_text='Дата поступления',
    )
    end_date = models.DateField(
        default=timezone.now(),
        null=True,
        blank=True,  # Если пусто - по настоящее время
        verbose_name='Дата окончания',
        help_text='Дата окончания',
    )
    faculty = models.CharField(
        null=True,
        blank=True,
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Факультет',
        help_text='Ваш факультет',
    )
    speciality = models.CharField(
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Специальность',
        help_text='Ваша специальность',
    )
    grade = models.CharField(
        null=True,
        blank=True,
        choices=GRADE,
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Степень',
        help_text='Ваша степень',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'student',
                    'university',
                    'start_date',
                    'end_date'
                    ],
                name='unique_university_in_one_time'),
        ]
        default_related_name = 'educations'
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        ordering = ('university', )

    def __str__(self):
        return (f'{self.student.first_name} {self.student.last_name} получал '
                f'образование по специальности "{self.speciality}"'
                f' в "{self.university}"')


class Information(models.Model):
    user = models.ForeignKey(
        ResumeUser,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        db_index=True,
    )
    about = models.TextField(
        verbose_name='О себе',
        help_text='Информация о себе, своих хобби и достижениях',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'about'],
                                    name='unique_about'),
        ]
        default_related_name = 'about'
        verbose_name = 'О себе'
        verbose_name_plural = 'О себе'
        ordering = ('about', )

    def __str__(self):
        return (f'{self.user.first_name} '
                f'{self.user.last_name} - ифнормация о себе.')


class Projects(models.Model):
    author = models.ForeignKey(
        ResumeUser,
        verbose_name='Автор проекта',
        on_delete=models.CASCADE,
        db_index=True,
    )
    name = models.CharField(
        verbose_name='Название проекта',
        help_text='Название проекта',
        max_length=USER_MODEL_MAX_LEN,
        null=True,
        blank=True,
        )
    info = models.TextField(
        verbose_name='Описание проекта',
        help_text='Краткое описание проекта',
        null=True,
        blank=True,
    )
    web_page = models.CharField(
        verbose_name='Ссылка на проект',
        help_text='Ссылка на проект',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'web_page'],
                                    name='unique_project'),
        ]
        default_related_name = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('web_page', )

    def __str__(self):
        return (f'Проект {self.web_page} пользователя '
                f'{self.author.first_name} {self.author.last_name}')
