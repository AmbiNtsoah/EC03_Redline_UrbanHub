from fastapi.testclient import TestClient

from src.validator import app
from src.ms_validateur_capteur.service import validate_sensor
from src.dto.request import SensorRequest
from src.dto.response import SensorResponse

client = TestClient(app)

def test_co2_normal():
    result = validate_sensor("co2", 500)
    assert result["level"] == "normal"


def test_co2_moderate():
    result = validate_sensor("co2", 900)
    assert result["level"] == "moderate"


def test_co2_critical():
    result = validate_sensor("co2", 1500)
    assert result["level"] == "critical"


def test_unknown_sensor():
    import pytest
    with pytest.raises(ValueError):
        validate_sensor("fake", 100)

def test_request_model():
    data = SensorRequest(sensor="co2", value=500)
    assert data.sensor == "co2"
    assert data.value == 500


def test_response_model():
    data = SensorResponse(
        valid=True,
        sensor="co2",
        value=500,
        level="normal",
        moderate_threshold=800,
        critical_threshold=1200,
        timestamp="now"
    )

    assert data.valid is True
    assert data.level == "normal"

def test_post_validate_normal():
    response = client.post(
        "/validate/",
        json={"sensor": "co2", "value": 500}
    )

    assert response.status_code == 200
    assert response.json()["level"] == "normal"


def test_post_validate_unknown_sensor():
    response = client.post(
        "/validate/",
        json={"sensor": "fake", "value": 100}
    )

    assert response.status_code == 400


def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200