import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "django_secret_key")

DEBUG = os.getenv("DEBUG", False)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(", ")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'resume.apps.ResumeConfig',
    'user.apps.UserConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "creating_and_editing_a_resume.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "creating_and_editing_a_resume.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

AUTH_USER_MODEL = 'user.ResumeUser'


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

DATE_INPUT_FORMATS = ["%d.%m.%Y"]

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BANNED_SYMBOLS = r'^[\w.@+-]+$'

USER_MODEL_MAX_LEN = 150

EMAIL_MAX_LEN = 254

GRADE = (
    ('Бакалавр', 'Бакалавр'),
    ('Магистр', 'Магистр'),
    ('Специалист', 'Специалист'),
    ('Кандидат наук', 'Кандидат наук',),
    ('Доктор наук', 'Доктор наук'),
)

RESOURCES = (
    ('GitHub', 'GitHub'),
    ('Behance', 'Behance'),
    ('Habr', 'Habr'),
    ('Персональная страничка', 'Персональная страничка'),
    ('StackOverflow', 'StackOverflow',),
)

STATUSES = (
    ('Активно ищу работу', 'Активно ищу работу'),
    ('Расммотрю предложения', 'Расммотрю предложения'),
    ('В творческом поиске', 'В творческом поиске'),
)