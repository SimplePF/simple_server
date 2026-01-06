import pytest
from fastapi.testclient import TestClient
from simple_server import app

@pytest.fixture
def client():
    return TestClient(app)
