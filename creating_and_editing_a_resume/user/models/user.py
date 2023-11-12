from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone


class ResumeUser(AbstractUser):
    """Model describing User"""

    email = models.EmailField(
        "email", unique=True, max_length=settings.EMAIL_MAX_LEN
    )
    phone = models.CharField(
        "Номер телефона",
        blank=True,
        validators=[
            RegexValidator(
                regex=settings.PHONE_REGEX,
                message="Проверьте корректно ли указан номер телефона",
            )
        ],
        help_text="Укажите номер телефона для связи",
    )
    telegram = models.CharField(
        "Telegram",
        blank=True,
        help_text="Аккаунт в Telegram. Начинается с @",
        validators=[
            RegexValidator(
                regex=settings.TELEGRAM_REGEX,
                message="Первый символ @, затем от 5 до 32 символов.",
            ),
        ],
    )
    city = models.CharField(
        verbose_name="Город",
        blank=True,
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Ваш город",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Ваша дата рождения",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"Пользователь {self.get_full_name()}"
