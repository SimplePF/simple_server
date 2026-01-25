import logging
from pydantic import BaseModel, field_validator

logger = logging.getLogger(__name__)

class PhysicalMeasurements(BaseModel):
    height: float
    weight: float

    @field_validator("height")
    @classmethod
    def validate_height(cls, v):
        if v <= 0:
            logger.error("Field 'height' must be greater than 0, height=%s", v)
            raise ValueError("height must be greater than 0.")
        return v

    @field_validator("weight")
    @classmethod
    def validate_weight(cls, v):
        if v <= 0:
            logger.error("Field 'weight' must be greater than 0, weight=%s", v)
            raise ValueError("weight must be greater than 0.")
        return v
