"""
[Prod] 실서버 등의 환경 설정 파일.
base.py 의 내용을 그대로 이어받고, 변경할 설정들만 다룬다.

(아직 미완성임. 사용하지 말 것)
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
        'ENGINE': 'mysql.connector.django',
        'NAME': os.getenv('DB_DATABASE'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}

# 커맨드라인에서 python manage.py collectstatic 을 필요로 함
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
