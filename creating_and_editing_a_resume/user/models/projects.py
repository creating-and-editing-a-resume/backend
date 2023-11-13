from core.enums import Limits
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Projects(models.Model):
    """Model describing user`s projects"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор проекта",
        db_index=True,
    )
    name = models.CharField(
        "Название проекта",
        help_text="Название проекта",
        max_length=Limits.USER_MODEL_MAX_LEN,
        blank=True,
    )
    info = models.TextField(
        "Описание проекта",
        help_text="Краткое описание проекта",
        blank=True,
    )
    web_page = models.URLField(
        "Ссылка на проект",
        max_length=Limits.URL_LEN,
        help_text="Ссылка на проект",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "web_page"], name="unique_project"
            ),
        ]
        default_related_name = "projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("web_page",)

    def __str__(self):
        return (
            f"Проект {self.web_page} пользователя "
            f"{self.author.get_full_name()}"
        )
