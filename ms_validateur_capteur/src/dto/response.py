from pydantic import BaseModel

class SensorResponse(BaseModel):
    valid: bool
    sensor: str
    value: float
    level: str
    moderate_threshold: float
    critical_threshold: float
    timestamp: str
