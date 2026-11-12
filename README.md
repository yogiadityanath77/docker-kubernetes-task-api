@"
# Docker and Kubernetes Task API

A FastAPI application built to learn containerization, CI/CD, Docker deployment, and Kubernetes.

## Features

- Health check endpoint
- Create tasks
- Retrieve all tasks
- Docker containerization
- Locust load testing

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | API status |
| GET | /health | Health check |
| POST | /tasks | Create a task |
| GET | /tasks | Retrieve all tasks |

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt