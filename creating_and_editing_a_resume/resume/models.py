from core.enums import Limits
from core.text import Text
from django.contrib.auth import get_user_model
from django.db import models
from user.models import about, courses, education, projects, work

User = get_user_model()


class Skills(models.Model):
    """Model describing skills"""

    skill = models.CharField(
        "Навык",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
    )
    profession = models.CharField(
        "Профессия",
        choices=Text.PROFESSIONS,
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        blank=True,
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ("id",)

    def __str__(self):
        return f"Навык {self.skill}"


class WebLink(models.Model):
    """Model describing web links"""

    name = models.CharField(
        "Интернет-ресурс",
        choices=Text.RESOURCES,
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Название сайта",
    )
    web_page = models.URLField(
        "Сайт",
        max_length=Limits.URL_LEN.value,
        help_text="Ссылка",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "web_page",
                ],
                name="unique_resource",
            ),
        ]
        verbose_name = "Ссылка на ресурс"
        verbose_name_plural = "Ссылки на ресурсы"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name} {self.web_page}"


class Resume(models.Model):
    """Model describing web resume"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        db_index=True,
    )
    updated = models.DateTimeField("updated", auto_now=True)
    search_status = models.CharField(
        "Статус поиска",
        choices=Text.STATUSES,
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Статус поиска",
        blank=True,
    )
    position = models.CharField(
        "Должность",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Должность",
    )
    image = models.ImageField(
        "Фото",
        upload_to="resume_images/",
        blank=True,
    )
    video_link = models.URLField(
        "Видео презентация",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Ссылка на видео с соискателем",
        blank=True,
    )
    created_at = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
        editable=False,
    )
    web_page = models.ManyToManyField(
        WebLink,
        verbose_name="Ссылки на свои ресурсы",
        blank=True,
    )
    skills = models.ManyToManyField(
        Skills,
        verbose_name="Навыки",
        blank=True,
    )
    works = models.ManyToManyField(
        work.EmploymentHistory,
        verbose_name="Место работы",
        blank=True,
    )
    courses = models.ManyToManyField(
        courses.Courses,
        verbose_name="Курсы",
        blank=True,
    )
    education = models.ManyToManyField(
        education.Education,
        verbose_name="Образование",
        blank=True,
    )
    about = models.ManyToManyField(
        about.Information,
        verbose_name="О себе",
        blank=True,
    )
    projects = models.ManyToManyField(
        projects.Projects,
        verbose_name="Проекты",
        blank=True,
    )

    class Meta:
        default_related_name = "resume"
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        ordering = ("-created_at",)

    def __str__(self):
        return f'Резюме для должности "{self.position}". Автор: {self.author}'
