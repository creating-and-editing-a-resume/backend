from core.enums import Limits
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Langeuage(models.Model):
    """Model describing user`s projects"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор проекта",
        db_index=True,
    )
    language = models.CharField(
        "Язык",
        help_text="Язык, которым вы владеете",
        max_length=Limits.USER_MODEL_MAX_LEN,
    )
    level = models.TextField(
        "Уровень",
        help_text="Уровень владения",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["language", "level"], name="unique_level"
            ),
        ]
        default_related_name = "languages"
        verbose_name = "Знание языка"
        verbose_name_plural = "Знание языков"

    def __str__(self):
        return (
            f'Знание языка "{self.language} пользователем '
            f"{self.author.get_full_name()}"
        )
