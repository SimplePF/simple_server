import pytest
from fastapi.testclient import TestClient

def test_read_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_calculate_bmi_endpoint_success(client: TestClient):
    """正常な入力によるBMI計算のテスト"""
    physical_measurements = {
        "height": 1.71,
        "weight": 70.50
    }
    response = client.post("/BMI", json=physical_measurements)

    assert response.status_code == 200
    assert response.json() == {"BMI": 24.11, "BMI_stats": "Normal weight"}

@pytest.mark.parametrize(
    "input_data, expected_bmi, expected_bmi_stats",
    [
        ({"height":1.57 ,"weight": 41.2}, 16.71,"Underweight"),
        ({"height":1.73 ,"weight": 89.6}, 29.94,"Overweight"),
        ({"height":1.81 ,"weight": 126.8}, 38.70,"Obesity"),
    ]
)
def test_calculate_bmi_endpoint_parametrized(client: TestClient, input_data, expected_bmi, expected_bmi_stats):
    """BMI計算をパラメータ化テストで複数ケース検証"""
    response = client.post("/BMI", json=input_data)
    assert response.status_code == 200
    result = response.json()
    assert result["BMI"] == expected_bmi
    assert result["BMI_stats"] == expected_bmi_stats

@pytest.mark.parametrize(
    "invalid_data, expected_status",
    [
        ({"height":0.0 ,"weight": 63.5}, 422),   #ゼロ除算
        ({"height":"invalid" ,"weight": 63.5}, 422),   #型エラー
        ({"height":"invalid"}, 422),   #Inputの欠如
    ]
)
def test_calculate_endpoint_invalid_input(client: TestClient, invalid_data, expected_status):
    """不正入力テスト"""
    response = client.post("/BMI", json=invalid_data)
    assert response.status_code == expected_status
