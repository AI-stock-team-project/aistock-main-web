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

## django 실행

django 실행

```console
python manage.py runserver
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
* /admin/ : 사이트 관리자
* /portfolios/ : 포트폴리오 기능
  * /portfolios/{portfolioId}/
* /stocks/{stockId}
* /equities/{종목명} : (예) /equities/samsung~




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