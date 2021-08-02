# 배포용 WebApplication 도커 파일

# slim-buster 는 데비안의 경량화 버전을 말함
FROM python:3.9.5-slim-buster
WORKDIR /app

# requirements.txt 를 먼저 복사함. 
COPY requirements.txt .

# pip 의존성 설치
RUN pip install -r requirements.txt

# cron 스케쥴링을 위한 부분 (cron, git)
RUN apt-get update && apt-get install -y cron git && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

# private git 을 이용하기 위해 ssh key 를 복사
RUN mkdir /root/.ssh/ \ 
  && touch /root/.ssh/known_hosts \
  && ssh-keyscan github.com >> /root/.ssh/known_hosts
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

# git clone and pip install
RUN git clone git@github.com:AI-stock-team-project/aistock-main-web.git web

# cron 스케쥴링 추가
# COPY .docker-config/production_cron_git_pull.sh ..
RUN echo "*/30 * * * * /bin/sh nobody -c 'cd /app/web && /usr/bin/git pull -q origin develop' >>/var/log/cron.log 2>&1" | crontab -

WORKDIR /app/web
COPY ./config/settings/dev.py ./config/settings/dev.py

# 장고 관련
RUN /bin/sh -c python manage.py migrate
RUN /bin/sh -c python manage.py createsuperuser --noinput