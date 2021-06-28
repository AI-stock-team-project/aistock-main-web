FROM python:3.9.5-slim-buster
WORKDIR /web
COPY . .
# mysqlclient 설치를 위해 필요한 부분들 apt-get install
RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
# pip 의존성 설치
RUN pip install -r requirements.txt
# 이미지를 생성할 때에는 'docker build -t django-test .' 같은 명령어를 이용.