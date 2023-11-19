from core.enums import Limits, Regex
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class ResumeUser(AbstractUser):
    """Model describing User"""

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=Limits.USER_NAME_MAX_LEN.value,
        help_text="Ваше имя",
        validators=[
            MinLengthValidator(
                Limits.USER_NAME_MIN_LEN.value,
            ),
        ],
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=Limits.USER_NAME_MAX_LEN.value,
        help_text="Ваша фамилия",
        validators=[
            MinLengthValidator(
                Limits.USER_NAME_MIN_LEN.value,
            ),
        ],
    )
    email = models.EmailField(
        "email", unique=True, max_length=Limits.EMAIL_MAX_LEN.value
    )
    phone = models.CharField(
        "Номер телефона",
        blank=True,
        validators=[
            RegexValidator(
                regex=Regex.PHONE_REGEX,
                message="Проверьте корректно ли указан номер телефона",
            ),
        ],
        help_text="Укажите номер телефона для связи",
    )
    profile_photo = models.ImageField(
        "Фото",
        upload_to="resume_images/",
        blank=True,
    )
    telegram = models.CharField(
        "Telegram",
        blank=True,
        help_text="Аккаунт в Telegram. Начинается с @",
        validators=[
            RegexValidator(
                regex=Regex.TELEGRAM_REGEX,
                message="Первый символ @, затем от 5 до 32 символов.",
            ),
        ],
    )
    city = models.CharField(
        verbose_name="Город",
        blank=True,
        max_length=Limits.CITY_MAX_LEN.value,
        help_text="Ваш город",
        validators=[
            MinLengthValidator(
                Limits.CITY_MIN_LEN.value,
            ),
        ],
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Ваша дата рождения",
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=Regex.BIRTH_DATE_REGEX,
                message="Дата должна быть в формате ДД.ММ.ГГГГ и не раньше 01.01.1930",
            ),
        ],
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"Пользователь {self.get_full_name()}"
