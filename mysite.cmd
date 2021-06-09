@echo off
REM cd c:/projects/mysite
REM 현재 경로로 이동
cd /D "%~DP0"

set DJANGO_SETTINGS_MODULE=config.settings.local

./venv/scripts/activate