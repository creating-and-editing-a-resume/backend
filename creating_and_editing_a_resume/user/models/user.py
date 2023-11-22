from core.enums import Limits, Regex
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import EmailValidator, RegexValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    """Changed method for creating user with email."""
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


class ResumeUser(AbstractUser):
    objects = CustomUserManager()
    """Model describing User"""
    username = None
    email = models.EmailField(
        "email",
        unique=True,
        max_length=50,
        validators=[
            EmailValidator(message="Введите корректный адрес электронной почты"),
            RegexValidator(
                regex=r'^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$',
                message="Только латинские буквы, цифры, тире, точка и нижнее подчеркивание. "
                        "Символ @ обязателен.",
            ),
        ],
    )
    phone = models.CharField(
        "Номер телефона",
        blank=True,
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+\d{1,3}\s?\(\d{3}\)\s?\(\d{3}-\d{2}-\d{2}\)$',
                message="Формат: +7 (...) (...-..-..)."
        )
        ],
    )
    telegram = models.CharField(
        "Telegram",
        blank=True,
        help_text="Аккаунт в Telegram. Начинается с @",
        validators=[
            RegexValidator(
                regex=r'^@[a-zA-Z0-9_]{5,32}$',
                message="Первый символ @, затем от 5 до 32 символов.",
            ),
        ],
    )
    city = models.CharField(
        verbose_name="Город",
        blank=True,
        max_length=50,
        help_text="Ваш город",
    )
    birth_date = models.CharField(
        verbose_name="Дата рождения",
        max_length=10,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\.\d{2}.\d{4}$',
                message='Дата рождения должна быть в формате дд.мм.гггг'
            ),
        ],
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"Пользователь {self.get_full_name()}"
