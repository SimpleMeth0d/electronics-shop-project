"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Умная колонка", 4999, 40)
item2 = Item('Телефон', 10000, 5)
Item.pay_rate = 0.9


def test_calculate_total_price():
    assert item1.calculate_total_price() == 199960


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 4499.1


def test_name():
    item2.name = 'Смартфон'
    assert item2.name == 'Смартфон'


def test_name_len13():
    item2.name = 'СуперСмартфон'
    assert item2.name == 'СуперСмар'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
