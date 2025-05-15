# FastAPI + Celery Microservice Example

A hands-on example demonstrating how to build a modern, containerized Python microservice with:

- **FastAPI** for high-performance HTTP & WebSocket endpoints  
- **Celery** for background task processing (Redis broker & result backend)  
- **PostgreSQL** via SQLAlchemy & Alembic migrations  
- **Jinja2** templates & **Bootstrap** for a simple form UI  
- **Broadcaster** + WebSockets for live task updates  
- **Docker Compose** for a fully isolated local development stack  
- Optional **Datadog Agent** integration for metrics & centralized logs  
- Built-in security scans (Bandit, Semgrep, pip-audit, Trivy) via GitHub Actions

---

## 🚀 Project Goals

1. Show how to cleanly separate web (FastAPI) and worker (Celery) concerns  
2. Provide synchronous **REST** + real-time **WebSocket** hooks for task status  
3. Illustrate container-based development with automatic reloads  
4. Enforce code quality & security best practices in CI/CD  
5. Offer a ready-to-fork template for future microservice projects

---

## 📦 Tech Stack

- Python 3.11  
- FastAPI, Uvicorn  
- Celery 5.x, Redis  
- SQLAlchemy 2.x, Alembic  
- Jinja2 + Bootstrap 5  
- broadcaster (WebSocket pub/sub)  
- Docker, Docker Compose  
- Datadog Agent (optional)  
- Bandit, Semgrep, safety, pip-audit, Trivy (security)

---

## 🛠️ Getting Started

### Prerequisites

Docker & Docker Compose  

### 1. Clone & Configure

```bash
git clone https://github.com/your-org/fastapi-celery-project.git
cd fastapi-celery-project
```
### 2. Build & Run

```bash
docker-compose up --build
```
### 3. Access the App
- **Web UI**: [http://localhost:8000](http://localhost:8000)
- **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Celery Flower**: [http://localhost:5555](http://localhost:5555)
- **PostgreSQL**: [http://localhost:5432](http://localhost:5432) (user: `postgres`, password: `postgres`)
- **Redis**: [http://localhost:6379](http://localhost:6379)


This work is mainly based on the [FastAPI + Celery Microservice Example](https://testdriven.io/).
