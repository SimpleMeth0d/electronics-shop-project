"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Умная колонка", 4999, 40)
Item.pay_rate = 0.9


def test_calculate_total_price():
    assert item1.calculate_total_price() == 199960


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 4499.1
