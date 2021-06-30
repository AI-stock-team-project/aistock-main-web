# production 셋팅용 도커 파일

# slim-buster 는 우분투의 경량화 버전을 말함
FROM python:3.9.5-slim-buster
WORKDIR /www/web
COPY . .
COPY production_cron_git_pull.sh ../

# mysqlclient 설치를 위해 필요한 부분들 apt-get install
RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential

# pip 의존성 설치
RUN pip install -r requirements.txt

# cron 스케쥴링을 위한 부분
RUN apt-get install -y cron && apt-get autoremove -y
RUN apt-get install -y git

