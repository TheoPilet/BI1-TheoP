from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_is_in_openapi_schema():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "/health" in response.json()["paths"]


def test_swagger_ui_is_available():
    response = client.get("/docs")

    assert response.status_code == 200
