from fastapi import APIRouter, HTTPException

from src.dto.request import SensorRequest
from src.ms_validateur_capteur.service import validate_sensor

router = APIRouter(prefix="/validate", tags=["Validator"])


@router.post("/")
def validate(data: SensorRequest):
    try:
        return validate_sensor(data.sensor, data.value)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))