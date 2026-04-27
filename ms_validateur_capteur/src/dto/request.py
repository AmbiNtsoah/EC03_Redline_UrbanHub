from pydantic import BaseModel

class SensorRequest(BaseModel):
    sensor: str
    value: float
    