import pytest
from simple_server.services.calculator import calculate_bmi, classify_bmi

@pytest.mark.parametrize(
    "height, weight, expected",
    [
        (1.48, 45.0, 20.54),
        (1.82, 115.8, 34.96),
        (1.623, 52.5, 19.93),
    ]
)
def test_calculate_bmi(height, weight, expected):
    result = calculate_bmi(height, weight)
    assert result == expected

@pytest.mark.parametrize(
    "bmi, expected",
    [
        (-1.0, "Invalid input value"),
        (0.0, "Underweight"),
        (15.8, "Underweight"),
        (21.3, "Normal weight"),
        (27.1, "Overweight"),
        (33.9, "Obesity"),
    ]
)
def test_classify_bmi(bmi, expected):
    result = classify_bmi(bmi)
    assert result == expected
