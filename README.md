# Phishing Detection System

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![Flask](https://img.shields.io/badge/Flask-API-111827)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)
![CI](https://img.shields.io/badge/GitHub_Actions-ready-2088FF)
![License](https://img.shields.io/badge/License-MIT-green)

Phishing Detection System is a recruiter-friendly cybersecurity portfolio project built with Python, Flask, URL feature extraction, ML-ready scoring. It provides a dashboard, REST API, persistence, tests, Docker support, and documentation that can be pushed as an individual GitHub repository.

## Features

- URL analysis
- ML classification
- Risk scoring
- Dashboard
- SQLite-backed result history
- REST API for analysis workflows
- Dashboard for recent findings
- CI workflow, issue templates, PR template, Dockerfile, and security notes

## Architecture

~~~mermaid
flowchart LR
    User[Analyst] --> Dashboard[Flask Dashboard]
    User --> API[REST API]
    API --> Engine[Analysis Engine]
    Engine --> DB[(SQLite)]
    Dashboard --> DB
    API --> Reports[JSON Results]
~~~

## Folder Structure

~~~text
.
+-- src
|   +-- app.py
|   +-- service.py
+-- templates
+-- static
+-- tests
+-- docs
+-- Dockerfile
+-- docker-compose.yml
+-- .github
~~~

## Installation

~~~bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python src/app.py
~~~

Open http://localhost:5000.

## API Documentation

POST /api/analyze accepts a JSON body and returns a scored analysis result.

Example:

~~~bash
curl -X POST http://localhost:5000/api/analyze -H "Content-Type: application/json" -d "{}"
~~~

GET /api/findings returns the latest stored analysis results.

GET /api/health returns service health.

## Testing Guide

~~~bash
pip install -r requirements.txt
pytest -q
~~~

## Docker Deployment

~~~bash
docker compose up --build
~~~

## Screenshots

Add screenshots after running the dashboard:

- Dashboard overview
- API response sample
- Findings history

## Security Considerations

- Use only on assets you own or are explicitly authorized to assess.
- Do not commit secrets or API keys.
- Add authentication before public exposure.
- Review logs for sensitive data before sharing demonstrations.

## Professional Commit Examples

- feat: add scored analysis workflow
- test: cover service scoring output
- docs: add deployment and security notes
