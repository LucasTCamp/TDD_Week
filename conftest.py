import pytest

@pytest.fixture
def player():
    return {"health": 70, "max_health": 100, "alive": True}

@pytest.fixture
def game():
    return { "score": 0, "multiplier": 1, "active": True}
