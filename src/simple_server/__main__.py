from fastapi import FastAPI
from .models import PhysicalMeasurements
from .services import calculator
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/BMI")
async def calculate_bmi_endpoint(physical_measurements: PhysicalMeasurements):
    bmi = calculator.calculate_bmi(physical_measurements.height, physical_measurements.weight)
    bmi_stats = calculator.classify_bmi(bmi)
    return {"BMI": bmi, "BMI_stats": bmi_stats}

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )
