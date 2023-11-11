from django.core.exceptions import ValidationError


def validate_starts_with(value):
    if value[0] != '@':
        raise ValidationError(f'Первый символ должен быть @!',
                              code='invalid',
                              params={'value': value})
