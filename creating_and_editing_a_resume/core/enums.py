from enum import IntEnum


class Limits(IntEnum):
    """Number constants."""

    EMAIL_MAX_LEN = 254
    USER_MODEL_MAX_LEN = 150
    URL_LEN = 2000


class Regex:
    """Regex data."""

    USER_NAME_REGEX = r"^[а-яА-ЯёЁ\s-]{2,50}$"
    PHONE_REGEX = r"^+[0-9]{10,12}$"
    TELEGRAM_REGEX = r"^[@][a-zA-Z\d_]{5,32}$"
    BANNED_SYMBOLS = r"^[\w.@+-]+$"
