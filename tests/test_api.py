import pytest
from fastapi.testclient import TestClient
from app.main import app, tasks

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear()
    yield
    tasks.clear()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn Docker", "completed": False}
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Learn Docker",
        "completed": False
    }


def test_get_tasks():
    client.post(
        "/tasks",
        json={"title": "Learn Kubernetes", "completed": False}
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert response.json()["tasks"][0]["title"] == "Learn Kubernetes"
