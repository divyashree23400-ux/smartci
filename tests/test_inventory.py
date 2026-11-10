import pytest
from src.inventory import Inventory

def test_add_stock():
    inv = Inventory()
    inv.add_stock('pen', 5)
    assert inv.stock['pen'] == 5

def test_remove_stock():
    inv = Inventory()
    inv.add_stock('pen', 5)
    inv.remove_stock('pen', 2)
    assert inv.stock['pen'] == 3

def test_remove_too_much():
    inv = Inventory()
    inv.add_stock('pen', 1)
    with pytest.raises(ValueError):
        inv.remove_stock('pen', 2)