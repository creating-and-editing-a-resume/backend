from django.db import models

from user.models import (ResumeUser, EmploymentHistory, Courses,
                         Education, Information, Projects,)
from creating_and_editing_a_resume.settings import (
    USER_MODEL_MAX_LEN,
    RESOURCES,
    STATUSES
    )


class Skills(models.Model):
    skill = models.CharField(
        verbose_name='Навык',
        max_length=USER_MODEL_MAX_LEN,
        )
    # После появления модели профессий тип поля нужно изменить
    profession = models.CharField(
        verbose_name='Профессия',
        max_length=USER_MODEL_MAX_LEN,
        null=True,
        blank=True,
        )

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ('id', )

    def __str__(self):
        return f'Навык {self.skill}'


class WebLink(models.Model):
    link_type = models.CharField(
        choices=RESOURCES,
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Интернет-ресурс',
        help_text='Название сайта',
    )
    web_page = models.CharField(
        verbose_name='Сайт',
        max_length=USER_MODEL_MAX_LEN,
        help_text='Ссылка',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'link_type',
                    'web_page',
                    ],
                name='unique_acount'),
        ]
        verbose_name = 'Ссылка на ресурс'
        verbose_name_plural = 'Ссылки на ресурсы'
        ordering = ('link_type',)

    def __str__(self):
        return f'{self.link_type} {self.web_page}'


class Resume(models.Model):
    author = models.ForeignKey(
        ResumeUser,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        db_index=True,
    )
    search_status = models.CharField(
        choices=STATUSES,
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Статус поиска',
        help_text='Статус поиска',
    )
    position = models.CharField(
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Должность',
        help_text='Должность',
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='resume_images/',
        null=True,
        blank=True
    )
    video_link = models.CharField(
        max_length=USER_MODEL_MAX_LEN,
        verbose_name='Видео презентация',
        help_text='Видео с соискателем',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        editable=False,
    )
    web_page = models.ManyToManyField(
        WebLink,
        verbose_name='Ссылки на свои ресурсы',
    )
    skills = models.ManyToManyField(
        Skills,
        verbose_name='Навыки',
    )
    works = models.ManyToManyField(
        EmploymentHistory,
        verbose_name='Место работы',
    )
    courses = models.ManyToManyField(
        Courses,
        verbose_name='Курсы',
    )
    education = models.ManyToManyField(
        Education,
        verbose_name='Образование',
    )
    about = models.ManyToManyField(
        Information,
        verbose_name='О себе',
    )
    projects = models.ManyToManyField(
        Projects,
        verbose_name='Проекты',
    )

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Резюме для должности "{self.position}". Автор: {self.author}'
