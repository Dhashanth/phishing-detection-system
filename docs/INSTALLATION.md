# Installation Guide

## Local Setup

~~~bash
python -m venv .venv
. .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
python src/app.py
~~~

Open http://localhost:5000.

## API Smoke Test

~~~bash
curl http://localhost:5000/api/health
curl -X POST http://localhost:5000/api/analyze -H "Content-Type: application/json" -d "{}"
~~~
