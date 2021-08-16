# 개발 환경, 로컬 환경에서의 Docker [도커 파일]

# slim-buster 는 데비안의 경량화 버전을 말함
FROM python:3.9.5-slim-buster
WORKDIR /app

# wget (dockerize에 필요) 설치
RUN  apt-get update \
    && apt-get install -y wget \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# DB 연결에 대기시킬 수 있는 기능을 하는 Dockerize 를 이용
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# requirements.txt 를 먼저 복사함. 
COPY requirements.txt .

# pip 의존성 설치
RUN pip install -r requirements.txt

# 소스 코드 복사
WORKDIR /app/web