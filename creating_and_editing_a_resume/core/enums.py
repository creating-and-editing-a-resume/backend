from enum import IntEnum


class Limits(IntEnum):
    """Number constants"""

    EMAIL_MAX_LEN = 50
    USER_MODEL_MAX_LEN = 150
    USER_NAME_MAX_LEN = 20
    USER_NAME_MIN_LEN = 2
    CITY_MAX_LEN = 25
    CITY_MIN_LEN = 2
    URL_LEN = 2000
    WORK_MIN_LEN = 2
    WORK_MAX_LEN = 50


class Regex:
    """Regex data"""

    TELEGRAM_REGEX = r"^[@][a-zA-Z\d_]{5,32}$"
    PHONE_REGEX = r"^([+7])[\d]{9,11}$"
    BANNED_SYMBOLS = r"^[\w.@+-]+$"
    BIRTH_DATE_REGEX = r"(?<!\d)(?:[0-9]|[12][0-9]|3[01]){2}.(?:[0-9]|1[0-2]){2}.(?:19[3-9][0-9]|20[01][0-9]){4}(?!\d)"
