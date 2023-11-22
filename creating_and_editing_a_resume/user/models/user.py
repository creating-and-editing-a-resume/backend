from core.enums import Limits, Regex
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        try:
            user.save(using=self._db)
        except Exception as e:
            raise ValueError(f"Unable to create account. Error: {str(e)}")

        return user


class ResumeUser(AbstractUser):
    """Model describing User"""

    objects = CustomUserManager()
    username = None

    email = models.EmailField(
        _("email"), unique=True, max_length=Limits.EMAIL_MAX_LEN.value
    )

    first_name = models.CharField(
        _("first name"),
        max_length=50,
        validators=[
            RegexValidator(
                regex=Regex.USER_NAME_REGEX,
                message="Check first name",
            ),
        ],
    )

    last_name = models.CharField(
        _("first name"),
        max_length=50,
        validators=[
            RegexValidator(
                regex=Regex.USER_NAME_REGEX,
                message="Check last name",
            ),
        ],
    )

    phone = models.CharField(
        _("phone number"),
        blank=True,
        max_length=12,
        validators=[
            RegexValidator(
                regex=Regex.PHONE_REGEX,
                message="Check phone number",
            ),
        ],
        help_text="Enter your phone number",
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
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Ваш город",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Ваша дата рождения",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"Пользователь {self.get_full_name()}"
