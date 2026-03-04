import pytest

@pytest.fixture
def player():
    return {"health": 70, "max_health": 100, "alive": True}
