from health import *

def test_take_damage(player):
    result = take_damage(player, 30)
    assert result["health"] == 40

def test_heal_adds_health(player):
    result = heal(player, 30)
    assert result["health"] == 100

def test_is_alive_true(player):
    result = take_damage(player, 100)
    assert result["alive"] == False