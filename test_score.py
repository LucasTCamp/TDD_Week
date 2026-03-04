import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points(game, amount):
    result = add_points(game, 5)
    assert result["score"] == 5

def test_add_points_rejects_negative(game):
    with pytest.raises(ValueError):
        add_points(game, -5)


def test_multiplier_updates(game, multiplier):
    result = apply_multiplier(game, 4)
    assert result["multiplier"] == 4


def test_multiplier_apply(game, multiplier):
    game["score"] = 5
    result = apply_multiplier(game, 2)
    assert result["score"] == 10

def test_apply_multiplier_greater_equal_1(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)

def test_no_multiplier_added_when_inactive(game):
    game["active"] = False
    game["score"] = 2
    result = apply_multiplier(game, 2)
    assert result["score"] == 2

def test_reset_score(game):
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"] == 1

def test_still_resets_inactive(game):
    game["active"] = False
    result = reset(game)
    assert result["score"] == 0 and result["multiplier"] == 1

def test_is_high_score(game, threshold):
    result = is_high_score(game, 5)
    if result["score"] > threshold:
        assert True
    else:
        assert False

def test_equal_high_score(game, threshold):
    result = is_high_score(game, 1)
    if result["score"] == threshold:
        assert False

def test_greater_equal_0_high_score(game, threshold):
    with pytest.raises(ValueError):
        apply_multiplier(game, -2)
