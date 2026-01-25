import logging

logger = logging.getLogger(__name__)

def calculate_bmi(height: float, weight: float):
    if weight == 0:
        logger.error("Division by zero attempted with height=%s, weight=%s", height, weight)
        raise ValueError("Division by zero is not allowed")
    return round(weight / height ** 2, 2)

def classify_bmi(bmi):
    if bmi < 0:
        return "Invalid input value"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"
