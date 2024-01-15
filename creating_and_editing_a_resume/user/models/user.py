from core.enums import Limits, Regex
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import EmailValidator, RegexValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    """Changed method for creating users without username."""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        try:
            user.save(using=self._db)
        except Exception as e:
            raise ValueError(f'Unable to create account. Error: {str(e)}')
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class ResumeUser(AbstractUser):
    objects = CustomUserManager()
    """Model describing User"""
    # username = None
    first_name = models.CharField(
        "Имя",
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-Я\s-]{2,50}$',
                message="Только кириллица, пробел или тире, длина от 2 до 50 символов.",
            ),
        ],
    )

    last_name = models.CharField(
        "Фамилия",
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-Я\s-]{2,50}$',
                message="Только кириллица, пробел или тире, длина от 2 до 50 символов.",
            ),
        ],
    )
    email = models.EmailField(
        "email",
        unique=True,
        max_length=50,
    )
    phone = models.CharField(
        "Номер телефона",
        blank=True,
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+7\d{10}$',
                message="Формат: +7 и 10-12 цифр.",
            )
        ],
    )
    telegram = models.CharField(
        "Telegram",
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^@[a-zA-Z0-9_]{5,32}$',
                message="Первый символ @, затем от 5 до 32 символов.",
            ),
        ],
    )
    city = models.CharField(
        "Город",
        blank=True,
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-Я\s-]{2,50}$',
                message="Только кириллица, пробел или тире, длина от 2 до 50 символов.",
            ),
        ],
        help_text="Ваш город",
    )
    birth_date = models.DateField(
        "Дата рождения",
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
