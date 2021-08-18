@echo off
REM 현재 경로로 이동
cd /D "%~DP0"

set DJANGO_SETTINGS_MODULE=config.settings.slim

./venv/scripts/activate