import pytest
from simple_server.models import PhysicalMeasurements


## 正常系テスト
def test_physical_measurements_valid_input():
    """正常な入力でモデル作成可能"""
    physical_measurements = PhysicalMeasurements(height=1.715, weight=63.1)
    assert physical_measurements.height == 1.715
    assert physical_measurements.weight == 63.1


@pytest.mark.parametrize(
    "height, weight",
    [
        (1.0, 1.0),      # 最小正値
        (100.0, 5000.0),   # 大値
        (2.14, 93.71),    # 小数
        (0.1, 0.01),     # 小数点以下
    ]
)
def test_physical_measurements_valid_boundary_values(height, weight):
    """境界値を含む正常系"""
    physical_measurements = PhysicalMeasurements(height=height, weight=weight)
    assert physical_measurements.height == height
    assert physical_measurements.weight == weight


## 異常系テスト（field_validator検証）
def test_height_zero_validation_error():
    """height=0で検証エラー"""
    with pytest.raises(ValueError, match="height must be greater than 0."):
        PhysicalMeasurements(height=0.0, weight=1.0)


def test_height_negative_validation_error():
    """heightが負数で検証エラー"""
    with pytest.raises(ValueError, match="height must be greater than 0."):
        PhysicalMeasurements(height=-1.0, weight=1.0)


def test_weight_zero_validation_error():
    """weight=0で検証エラー"""
    with pytest.raises(ValueError, match="weight must be greater than 0."):
        PhysicalMeasurements(height=1.0, weight=0.0)


def test_weight_negative_validation_error():
    """weightが負数で検証エラー"""
    with pytest.raises(ValueError, match="weight must be greater than 0."):
        PhysicalMeasurements(height=1.0, weight=-1.0)


## 同時エラーケース
def test_both_height_and_weight_invalid():
    """height,weight両方無効"""
    with pytest.raises(ValueError, match="height must be greater than 0."):  # heightが先に検証される
        PhysicalMeasurements(height=0.0, weight=0.0)


@pytest.mark.parametrize(
    "invalid_data",
    [
        (0.0, 1.0),   # height=0
        (-1.0, 52.0),  # height負数
        (1.0, 0.0),   # weight=0
        (1.65, -1.0),  # weight負数
    ]
)
def test_all_validation_errors(invalid_data):
    """全異常系をパラメータ化"""
    height, weight = invalid_data
    with pytest.raises(ValueError):
        PhysicalMeasurements(height=height, weight=weight)
