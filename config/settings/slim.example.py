"""
[Local-Slim 버전]
- Docker 없이, MySQL 없이 사용할 경우
- sqlite를 이용해서 간단히 설치해서 테스트할 수 있는 모드이다.
"""
# noinspection PyUnresolvedReferences
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# local-slim.py 로 복사한 후에 SECRET_KEY를 입력해준다.
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
