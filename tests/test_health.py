from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_capabilities_endpoint_never_overclaims():
    response = client.get("/api/v1/invoices/capabilities")
    assert response.status_code == 200
    payload = response.json()
    assert payload["ocr"] is False
    assert payload["pdf_text_extraction"] is False
    assert payload["official_validation"] is False
