import pytest
from inventory import add_item, remove_item, get_item_count


def test_add_item(empty_inventory):
    result = add_item(empty_inventory, "Sword")
    assert "Sword" in result["items"]

def test_add_item_rejects_empty_item(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, "")

def test_add_item_rejects_full_inventory(full_inventory):
    with pytest.raises(ValueError):
        add_item(full_inventory, "Whatever")

def test_add_item_doesnt_change_locked_inventory(locked_inventory):
    result = add_item(locked_inventory, "shield")
    assert "shield" not in result["items"]

def test_remove_item(empty_inventory):
    empty_inventory["items"] = ["b", "a", "b"]
    result = remove_item(empty_inventory, "b")
    assert result["items"] == ["a", "b"]

def test_remove_item_rejects_not_there_item(full_inventory):
    with pytest.raises(ValueError):
        remove_item(full_inventory, "b")

def test_remove_item_doesnt_change_locked_inventory(locked_inventory):
    result = remove_item(locked_inventory, "sword")
    assert "sword" in result["items"]

def test_get_item_count(full_inventory):
    result = get_item_count(full_inventory)
    assert result == 10

def test_get_item_count_returns_zero(empty_inventory):
    result = get_item_count(empty_inventory)
    assert result == 0

def test_get_item_count_returns_count_locked_inventory(locked_inventory):
    result = get_item_count(locked_inventory)
    assert result == 10


    
