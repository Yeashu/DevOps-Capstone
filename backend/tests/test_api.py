import pytest

pytestmark = pytest.mark.integration


def save(client, expression="sqrt(144) + 2^3", **kwargs):
    return client.post("/api/calculations", json={"expression": expression, **kwargs})


def test_health_and_migrated_readiness(client):
    assert client.get("/health").json()["status"] == "ok"
    assert client.get("/api/health").status_code == 200
    assert client.get("/ready").status_code == 200


def test_create_calculation(client):
    response = save(client)
    assert response.status_code == 201
    assert response.json()["result"] == 20
    assert response.json()["created_at"]


def test_list_and_read_calculation(client):
    row = save(client).json()
    assert client.get("/api/calculations").json() == [row]
    assert client.get(f'/api/calculations/{row["id"]}').json() == row


def test_update_label_preserves_result(client):
    row = save(client).json()
    response = client.put(f'/api/calculations/{row["id"]}', json={"label": "  Lab result  "})
    assert response.status_code == 200
    assert response.json()["label"] == "Lab result"
    assert response.json()["result"] == 20


def test_delete_calculation(client):
    row = save(client).json()
    assert client.delete(f'/api/calculations/{row["id"]}').status_code == 204
    assert client.get(f'/api/calculations/{row["id"]}').status_code == 404
    assert client.get("/api/calculations").json() == []


def test_preview_does_not_save(client):
    response = client.post("/api/evaluate", json={"expression": "sin(30)", "angle_mode": "deg"})
    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(.5)
    assert client.get("/api/calculations").json() == []


@pytest.mark.parametrize("payload", [
    {"expression": "1/0"}, {"expression": "sqrt(-1)"}, {"expression": ""},
    {"expression": "__import__('os')"}, {"expression": "1", "angle_mode": "bad"},
    {"expression": "1", "label": "a" * 81}, {"expression": "1" * 257},
])
def test_invalid_input_is_not_persisted(client, payload):
    assert client.post("/api/calculations", json=payload).status_code == 422
    assert client.get("/api/calculations").json() == []


def test_pagination_order_and_validation(client):
    first = save(client, "1").json()
    second = save(client, "2").json()
    assert client.get("/api/calculations?limit=1").json() == [second]
    assert client.get("/api/calculations?offset=1").json() == [first]
    assert client.get("/api/calculations?limit=0").status_code == 422


def test_missing_records(client):
    assert client.put("/api/calculations/999", json={"label": "X"}).status_code == 404
    assert client.delete("/api/calculations/999").status_code == 404


def test_metrics_include_request_counter_and_latency(client):
    client.post("/api/evaluate", json={"expression": "2+2"})
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
    assert "orbit_http_requests_total" in response.text
    assert "orbit_http_request_duration_seconds_bucket" in response.text


def test_readiness_fails_when_database_is_unavailable(client, monkeypatch):
    from sqlalchemy.exc import OperationalError
    from unittest.mock import Mock
    import app.main as main

    unavailable = Mock()
    unavailable.connect.side_effect = OperationalError("SELECT 1", {}, Exception("offline"))
    monkeypatch.setattr(main, "engine", unavailable)
    assert client.get("/ready").status_code == 503
    assert client.get("/health").status_code == 200
