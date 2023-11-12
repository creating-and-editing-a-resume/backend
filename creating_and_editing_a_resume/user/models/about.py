from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Information(models.Model):
    """Model describing about user block"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Пользователь",
    )
    about = models.TextField(
        "О себе",
        help_text="Информация о себе, своих хобби и достижениях",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "about"], name="unique_about"
            ),
        ]
        default_related_name = "about"
        verbose_name = "О себе"
        verbose_name_plural = "О себе"

    def __str__(self):
        return f"{self.user.get_full_name()} - информация о себе."
