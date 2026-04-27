from features.validator.service import validate_sensor


def test_co2_normal():
    result = validate_sensor("co2", 500)
    assert result["level"] == "normal"


def test_co2_moderate():
    result = validate_sensor("co2", 900)
    assert result["level"] == "moderate"


def test_co2_critical():
    result = validate_sensor("co2", 1500)
    assert result["level"] == "critical"