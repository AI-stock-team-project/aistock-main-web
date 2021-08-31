# AI Stock 예측 프로젝트
인공지능 주식 예측 프로젝트입니다. 

(요약 설명)



# 개요 
(설명이 들어가야 하는 부분)



# 설치된 패키지
* `pip install django` : sqlparse, pytz, asgiref, django
* `pip install mysql-connector-python` : protobuf
* `pip install django-settings-export` : django-settings-export
* `pip install factory-boy` : text-unidecode, python-dateutil, Faker, factory-boy

`requirements.txt` 참고


# git 으로 코드를 내려받기
서브모듈을 포함하고 있으므로, 서브모듈에 대한 명령어도 같이 포함.

```
git clone --recursive https://github.com/AI-stock-team-project/aistock-main-web.git <폴더명>
cd <폴더명>
git submodule foreach --recursive git checkout master
```



만약, 단순히 git clone 만 했을 때에, data-api 폴더가 비어있다면 (서브모듈을 내려받지 못했다면) 다음의 명령어로 data-api 폴더 내의 파일을 내려받기
```
git submodule update --init --recursive
git submodule foreach --recursive git checkout master
```



# 개발 환경 셋팅
docker를 이용하여 구동환경을 맞춰주고, 개발도구(PyCharm 또는 VSCode)로 작업을 진행한다.

환경 셋팅하는 순서
1. 장고 설정하기 
    1. `/config/settings/local.example.py`을 복사해서 `/config/settings/local.py`를 새로 만든다.
    2. 설정파일(`local.py`)에서 입력해줘야 할 것들
        * `SECRET_KEY`설정 : `python config/settings/generate_secretkey.py` 커맨드를 실행하면 키를 랜덤하게 생성해주는데, 생성된 키 값을 복사해서 넣어주도록 한다.
2. 도커 환경변수 설정하기
    1. `_docker` 폴더에서 `.local.env.example`을 복사해서 `.local.env`파일을 새로 만든다.
    2. 위의 설정 파일(`.local.env`)에서 다음을 입력해준다.
        - MYSQL_ROOT_PASSWORD : MYSQL의 루트계정 비밀번호 (복잡한 랜덤한 비밀번호를 넣어주면 됨)
        - MYSQL_PASSWORD : 장고에 이용할 MYSQL의 비밀번호 (복잡한 랜덤한 비밀번호를 넣어주면 됨)
        - DJANGO_SUPERUSER_USERNAME : 장고 최고관리자의 아이디
        - DJANGO_SUPERUSER_EMAIL : 장고 최고관리자의 이메일
        - DJANGO_SUPERUSER_PASSWORD : 장고 최고관리자의 비밀번호
    3. 도커 이미지 및 컨테이너를 생성하면서 실행
        ```console
        docker-compose --env-file=_docker/.local.env up --build --force-recreate -d
        ```
    4. 자동으로 실행이 된다. 접속은 http://localhost:18000
    5. 재생성을 해야하는 경우에는 3번을 하기 전에 다음의 명령어를 한 후에 한다.
        (db 볼륨 삭제)
        ```console
        docker-compose --env-file=_docker/.local.env down -v
        ```
        (컨테이너 및 이미지, 볼륨 재생성)
        ```console
        docker-compose --env-file=_docker/.local.env up --build --force-recreate -d
        ```


알아둘 사항
* 도커에서 DB를 볼륨으로 생성하였기 때문에, 이후에 다시 생성하여도 변경값이 적용되지 않을 수 있음. 이 경우 해당 볼륨을 삭제 후 진행을 하면 됨.
* 윈도우의 도커에서 Compose의 중지,재시작,삭제 등이 안 될 수 있는데, 각각의 컨테이너를 중지,재시작을 하면 동작이 됨.


# 구성
## 폴더 구성
기본 구성
* config : 설정
* templates : front-end (view) 
* static : css, js, images 등

추가된 구성
* stock : 주가 종목 정보
