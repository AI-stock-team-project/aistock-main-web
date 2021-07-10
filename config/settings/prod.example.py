"""
로컬 설정 파일.
base.py 의 내용을 그대로 이어받고, local 에서만 변경할 설정들을 다룬다.
"""
# noinspection PyUnresolvedReferences
from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1', '0.0.0.0']

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_DATABASE'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}

# 커맨드라인에서 python manage.py collectstatic 을 필요로 함
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
