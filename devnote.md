# 이 프로젝트에서 Docker 생성하기
용어 참고(https://en.wikipedia.org/wiki/Deployment_environment)
- local : 개발자 환경, 로컬 환경에서 구동할 때
- dev : 개발 서버, 개발자들끼리 공통된 작업을 테스트하는 서버에서 구동할 때
- prod (production) : 실 서버, 실제 서버에서 구동할 때


## local 모드

준비 과정
* config/settings/local.py 생성 및 설정
* _docker/.local.env 생성 및 설정

주의 사항
* 작업중인 폴더를 마운트할 것이므로, 향후 경로가 변경되지 않아야 함. (아주 적절한 위치에 코드를 위치시키고 작업할 것을 권장)


docker-compose 생성 및 실행(dev)
```console
docker-compose --env-file=_docker/.local.env up --build --force-recreate -d
```


참고
* 'mysql'만 도커로 생성하고 싶을 때에는 다음 커맨드 사용
    `docker run --env-file=./.docker-config/.dev.env --name aistock-mysql-only -p 33306:3306 -d mysql:8.0`


## dev 모드 (개발서버 모드)
준비 과정
* config/settings/prod.py 생성 및 설정
* .docker-config/.prod.env 생성 및 설정
* .docker-config/id_rsa 생성. (ssh-keygen 으로 생성된 id_rsa 또는 갖고있던 id_rsa 를 위치시켜야 한다)(비공개 git 저장소를 이용하기 위함)

주의 사항
* 작업중인 폴더를 마운트할 것이므로, 향후 경로가 변경되지 않아야 함. (아주 적절한 위치에 코드를 위치시키고 작업할 것을 권장)


docker-compose 생성 및 실행(prod)
```console
docker-compose --env-file=_docker/.dev.env up --build --force-recreate -d
```

docker-compose 중지
```console
docker-compose --env-file=_docker/.dev.env stop
```

docker-compose 중지된 것을 시작
```console
docker-compose --env-file=_docker/.dev.env start
```

# docker 없이 작업할 때에
1. MySQL 설치 및 데이터베이스 생성 (mysql에서 데이터베이스를 생성한다)
    - 데이터베이스를 생성해주고, 유저를 생성해주고, 유저에게 데이터베이스에 대한 권한을 설정해준다.
2. 장고 설정
    - /config/settings/local.py 를 만들어준다.
    - SECRET_KEY 및 DATABASE 설정을 해준다.
        - `python config/settings/generate_secretkey.py`을 통해서 SECRET_KEY를 생성할 수 있음
3. 파이썬 가상환경 셋팅
    1. pycharm의 경우) 알아서 셋팅이 된다. requirements 를 읽어오면서 셋팅을 한다. 'Creating Virtual Environment'창이 뜨면서 확인을 누르면 알아서 됨.
    2. vscode의 경우) `python -m venv venv`을 통해서 venv폴더를 생성 (주의: powershell 터미널은 안 되고, 일반 터미널로 해야함)
4. 패키지 설치
    1. pycharm의 경우) 알아서 됨.
    2. vscode의 경우) 
        ```console
        mysite
        pip install -r requirements.txt
        ```
5. 장고 웹서버 실행하기
    ```console
    mysite
    python manage.py runserver
    ```

참고
* `mysite`는 파이썬 가상환경을 셋팅해주는 스크립트이다.
* 윈도우 환경에서는 파이썬 64비트를 권장함
  


# 자주 사용되는 명령어
## Docker
### Dockerfile 로 Docker 생성
구문 (Dockerfile -> Docker image 생성)
```console
docker build -t (이미지이름) (경로. 보통 '.'으로 현재폴더를 가리킴)
```


예시)
```console
docker build -t aistoc-web-dev001 .
```


예시2) Dockerfile 명을 지정해줘야 할 때
```console
docker build -f Dockerfile.dev -t aistoc-web-dev001 .
```



### docker-compose 명령어
실행 및 컨테이너 생성
```console
docker-compose up
```


정지 및 컨테이너 삭제
```console
docker-compose down
```


이미지 빌드와 동시에 실행
```console
docker-compose up --build
```


이미지 빌드와 동시에 실행 (+백그라운드 실행)
```console
docker-compose up --build -d
```
설명
* up : docker-compose로 생성된 이미지들을 컨테이너로 실행한다는 의미
* --build : 빌드를 해주면서 실행하겠다는 의미
* -d : 백그라운드로 실행한다는 의미
* 여기서 env 로는 기본값으로 `.env`파일이 있다면 사용하게 된다. 없으면 사용하지 않는다.
* 여기서 yml 파일은 기본값으로 `docker-compose.yml`파일을 사용하게 된다.


```console
docker-compose --env-file=(env파일 경로) up --build --force-recreate -d
```
설명
* --env-file : env파일을 수동으로 지정하겠다는 의미
* --force-recreate : 기존에 같은 명칭으로 생성한 docker이미지가 있다면 지우고 다시 만들겠다는 의미



## django
### django 실행

```console
python manage.py runserver
```

### migrate 
테이블을 데이터베이스에 적용시킬 때
```console
python manage.py migrate
```



## 파이썬 패키지 관리
### requirements.txt
requirements.txt 생성 및 갱신
```console
pip freeze > requirements.txt
```

requirements.txt 로부터 패키지 설치
```console
pip install -r requirements.txt
```



### pip
파이썬 패키지 추가/설치
```console
pip install (패키지명)
```

설치된 패키지 목록 조회
```console
pip list
```

업데이트 가능한 것 조회
```console
pip list --outdated
```



# 구성
## 폴더 구성
기본 구성
* config : 설정
* templates : front-end (view) 
* static : css, js, images 등

추가된 구성
* stock : 주가 종목 정보


## URL 구성
기능
* /portfolios/ : 포트폴리오 기능
    * /portfolios/{portfolioId}/
* /stocks/{stockId}
* /equities/{종목명} : (예) /equities/samsung~


기본
  * /logout : 로그아웃 
  * /login : 로그인
  * /signup : 가입
  * /admin/ : 사이트 최고 관리자



## 서비스 구성
Account(유저 정보 기능)
* 회원가입/탈퇴, 로그인/로그아웃, 정보변경


Admin(관리자 기능)
* 


메인 페이지
* 코스피 정보
* 최근 뉴스


포트폴리오 관리
* 포트폴리오 추천 기준 선택
* 포트폴리오 목록 관리 : 포트폴리오 추가/삭제/이름 변경
* 포트폴리오의 종목 관리
    * 종목 추가/삭제

주식 종목 조회
* 주식 종목 전체 보기
* 주식 종목 검색
* 주식 종목 갱신 (새로 받아옴)


주식 가격 조회
* 주식 항목 선택 후 > 가격 조회



## 데이터베이스 구성
유저 테이블 auth_user
* id

주가 종목 테이블
* id (종목 key)
* 종목명 
* code (짧은 종목코드) : 숫자 6자리의 짧은 형태의 종목 코드.  
* expcode (긴 종목코드) : 'KR7003670007'같은 긴 형태의 종목 코드.
* is_eft (ETF 유무) : ETF 인지 여부.


주가 시세 테이블


포트폴리오 테이블 (유저 x 주가 종목)
* user_id
* 