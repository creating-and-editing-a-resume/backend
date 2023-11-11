from django.conf import settings
from django.core.exceptions import ValidationError


def validate_starts_with(value):
    if value[settings.FIRST_SYMBOL] != '@':
        raise ValidationError('Первый символ должен быть @!',
                              code='invalid',
                              params={'value': value})
