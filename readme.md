# AI Stock 예측 프로젝트
인공지능 주식 예측 프로젝트입니다. 

(요약 설명)



# 개요 
(설명이 들어가야 하는 부분)



# 설치
## 사용된 라이브러리
`requirements.txt`에 기술됨
* django (asgiref, pytz, sqlparse 포함됨)
* mysqlclient



## 개발 환경 셋팅
### PyCharm (권장)
패키지 설치 : PyCharm 으로 구동하면 requirements.txt 를 통해서 패키지를 설치하며 'venv' 폴더를 자동적으로 생성한다.


### VSCode
PyCharm을 통해서 'venv' 폴더가 생성된 이후라면, VSCode 로 작업이 가능하다.

pip나 python을 VSCode 하단의 터미널(powershell은 안 됨에 주의)에서 사용하려면 다음과 같은 과정을 거친다.
1. (커맨드에서) `mysite`
2. (커맨드에서) 앞부분에 '(venv)'가 있는 것을 확인하고, python 명령이나 django 명령어, pip 명령어 등을 사용할 수 있다. 



## 서버 실행
### (공통) local.py 환경설정 만들기

1. `./config/settings/local.example.py`을 복사해서 `./config/settings/local.py`를 새로 만든다.
2. 위의 설정파일(`local.py`)에서 입력해줘야 할 것들
    * `SECRET_KEY`설정 : 다음의 커맨드를 실행하면 키를 랜덤하게 생성해주는데, 이 키를 복사해서 넣어주도록 한다.
        ```console
        python config/settings/generate_secretkey.py
        ```
    * `DATABASES` : 데이터베이스 연결을 위한 설정을 입력해준다. (Docker 사용시에는 변경하지 않고 그대로 둠)



### (CASE - 1) 도커 사용시
1. 도커를 설치한다.
2. `.docker-config` 폴더에서 `.dev.env.example`을 복사해서 `.dev.env`파일을 새로 만든다.
3. 위의 설정 파일(`.dev.env`)에서 변경해줘야 할 것들
    - MYSQL_ROOT_PASSWORD, MYSQL_PASSWORD를 아무렇게나 입력해준다. (사용할 비밀번호가 됨)
4. 도커 이미지 및 컨테이너를 포함하는 'docker compose'를 생성한다.
    ```console
    docker-compose --env-file=./.docker-config/.dev.env up --build --force-recreate -d
    ```
5. 자동으로 실행이 된다.



### (CASE - 2) 데이터베이스 설치하고, 파이썬 가상환경으로 패키지 구성할 경우

1. MySQL을 설치한다.
    - 데이터베이스를 생성해주고, 유저를 생성해주고, 유저에게 데이터베이스에 대한 권한을 설정해준다.
2. `config/settings/local.py`에서 해당 데이터베이스에 대한 연결 설정을 해준다.
3. 파이썬 가상 환경 생성 및 패키지 설치
    * `PyCharm`의 경우) 디렉토리를 열면 'Creating Virtual Environment'창이 뜨면서 확인을 누르면 `venv`를 생성하면서 관련 패키지까지 설치해준다.
    * `PyCharm`이 아닌 경우)
        ```console
        python -m venv venv
        mysite
        pip install -r requirements.txt
        ```
3. 서버 실행하기
    ```console
    mysite
    python manage.py runserver
    ```

참고
* `mysite`는 파이썬 가상환경을 셋팅해주는 스크립트이다.
* 윈도우 환경에서는 파이썬 64비트를 권장함(mysqlclient 이슈로 인함)


# 구성
## 폴더 구성
기본 구성
* config : 설정
* templates : front-end (view) 
* static : css, js, images 등

추가된 구성
* stock : 주가 종목 정보