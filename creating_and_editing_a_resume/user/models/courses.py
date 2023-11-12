from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Courses(models.Model):
    """Model describing courses experience"""

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Студент курсов",
        db_index=True,
    )
    company = models.CharField(
        "Организация",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Название организации проводившей обучение",
    )
    name = models.CharField(
        "Название курса",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Название курса",
    )
    date = models.DateField(
        "Дата окончания курсов",
        help_text="Дата окончания курсов",
    )
    speciality = models.CharField(
        "Специальность",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Ваша специальность",
    )
    experience = models.TextField(
        "Опыт",
        help_text="Полученный вами опыт",
    )
    skills = models.TextField(
        "Навыки",
        help_text="Полученные вами навыки",
    )
    diploma_link = models.URLField(
        "Ссылка на проект/дипломную работу",
        max_length=settings.URL_LEN,
        blank=True,
        help_text="Ссылка на проект/дипломную работу",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "company", "name", "date"],
                name="unique_course_in_one_time",
            ),
        ]
        default_related_name = "courses"
        verbose_name = "Повышение квалификации"
        verbose_name_plural = "Повышение квалификации"
        ordering = ("-date",)

    def __str__(self):
        return (
            f"{self.student.get_full_name()}"
            f' повышал квалификацю "{self.name}" в "{self.company}"'
        )
