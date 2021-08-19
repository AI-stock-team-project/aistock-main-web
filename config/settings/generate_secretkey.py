import secrets
RANDOM_STRING_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


def get_random_secret_key(length=50, allowed_chars=RANDOM_STRING_CHARS):
    """
    django/core/management/utils.py 의 get_random_secret_key
    django/utils/crypto.py 의 get_random_string
    두 파일을 참조
    """
    return ''.join(secrets.choice(allowed_chars) for _ in range(length))


print('django-insecure-' + get_random_secret_key())
