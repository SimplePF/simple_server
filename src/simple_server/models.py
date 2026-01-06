from pydantic import BaseModel, field_validator

class PhysicalMeasurements(BaseModel):
    height: float
    weight: float

    @field_validator("height")
    @classmethod
    def validate_height(cls, v):
        if v <= 0:
            raise ValueError("height must be greater than 0.")
        return v

    @field_validator("weight")
    @classmethod
    def validate_weight(cls, v):
        if v <= 0:
            raise ValueError("weight must be greater than 0.")
        return v
