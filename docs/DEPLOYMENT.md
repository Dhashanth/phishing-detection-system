# Deployment Guide

## Local

~~~bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python src/app.py
~~~

## Docker

~~~bash
docker compose up --build
~~~

## Production Notes

- Put the app behind a reverse proxy.
- Add authentication and rate limiting before internet exposure.
- Use managed logging and secrets.
