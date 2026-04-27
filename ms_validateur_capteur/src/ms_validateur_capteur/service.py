from datetime import datetime, UTC
from src.domain.rules import THRESHOLDS

def validate_sensor(sensor: str, value: float) -> dict:
    if sensor not in THRESHOLDS:
        raise ValueError("Unknown sensor")

    limits = THRESHOLDS[sensor]

    if value < limits["moderate"]:
        level = "normal"
    elif value < limits["critical"]:
        level = "moderate"
    else:
        level = "critical"

    return {
        "valid": True,
        "sensor": sensor,
        "value": value,
        "level": level,
        "moderate_threshold": limits["moderate"],
        "critical_threshold": limits["critical"],
        "timestamp": datetime.now(UTC).isoformat(),
    }