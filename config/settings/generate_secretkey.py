from django.core.management.utils import get_random_secret_key
print('django-insecure-' + get_random_secret_key())
