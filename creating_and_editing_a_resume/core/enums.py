from enum import IntEnum


class Limits(IntEnum):
    """Number constants"""

    EMAIL_MAX_LEN = 254
    USER_MODEL_MAX_LEN = 150
    URL_LEN = 2000


class Regex:
    """Regex data"""

    TELEGRAM_REGEX = r"^[@][a-zA-Z\d_]{5,32}$"
    PHONE_REGEX = r"^([+7]|[8])[\d]{7,11}$"
    BANNED_SYMBOLS = r"^[\w.@+-]+$"
