# AI Stock 예측 프로젝트
이 저장소는 'AI Stock 예측 프로젝트'의 웹 서비스 파트만을 다루는 저장소입니다.


# 필요한 라이브러리
`requirements.txt`에 기술됨
* django (asgiref, pytz, sqlparse 포함됨)
* mysqlclient


# 셋팅
## 개발 환경 셋팅
### 공통
#### local.py 환경설정 만들기
`./config/settings/local.py`를 새로 만든다.

(local.py)
```python
"""
로컬 설정 파일.
base.py 의 내용을 그대로 이어받고, local 에서만 변경할 설정들을 다룬다.
"""
# noinspection PyUnresolvedReferences
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```
위와 같은 형태로 만들어준다. 


위의 설정파일에서 입력해줘야 할 것들
1. SECRET_KEY : `config/settings/generate_secretkey.py`를 파이썬으로 실행(`python config/settings/generate_secretkey.py`하면 키를 랜덤하게 생성해주는데, 이 키를 복사해서 넣어주도록 한다.
2. DATABASES : 데이터베이스 연결을 위한 설정을 입력해준다.


(CASE1) 만약 데이터베이스를 직접 설치하고 위에서 설정한 경우라면, 다음의 명령어를 통해서 웹서버를 실행할 수 있다.
1. (커맨드에서) `mysite`
2. (커맨드에서) `python manage.py runserver`


(CASE2) 도커를 이용해서 셋팅한 상태라면, 그냥 도커를 실행하면 된다.



### PyCharm (권장)
패키지 설치 : PyCharm 으로 구동하면 requirements.txt 를 통해서 패키지를 설치하며 'venv' 폴더를 생성한다.



### VSCode
PyCharm을 통해서 'venv' 폴더가 생성된 이후라면, VSCode 로 작업이 가능하다.



## Dockerfile 로 Docker 생성 (미완성)

```console
docker build -t (이미지이름) (경로. 보통 '.'으로 현재폴더를 가리킴)
```

예시
```console
docker build -t aistock-web-dev001 .
```


# 구성
## 폴더 구성
기본 구성
* config : 설정
* templates : front-end (view) 
* static : css, js, images 등

추가된 구성
* stock : 주가 종목 정보