import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from .logger_config import setup_logging
from .models import PhysicalMeasurements
from .services import calculator

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}

@app.post("/BMI")
async def calculate_bmi_endpoint(physical_measurements: PhysicalMeasurements):
    logger.info(
        "Calculation of BMI request received: height=%s, weight=%s",
        physical_measurements.height, physical_measurements.weight)
    try:
        bmi = calculator.calculate_bmi(physical_measurements.height, physical_measurements.weight)
        bmi_stats = calculator.classify_bmi(bmi)
        logger.info("Calculation of BMI completed: BMI=%s, BMI_stats=%s", bmi, bmi_stats)
        return {"BMI": bmi, "BMI_stats": bmi_stats}
    except ValueError as e:
        logger.warning("Calculation of BMI failed: %s", e)
        raise HTTPException(status_code=422, detail=e) from e

def main():
    setup_logging()
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
