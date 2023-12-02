"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError

item1 = Item("Умная колонка", 4999, 40)
item2 = Item('Телефон', 10000, 5)
item3 = Item("Смартфон", 10000, 20)
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
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    assert repr(item3) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item3) == 'Смартфон'


def test_empty_csv():
    """Тестирование ненайденного файла"""
    file_name = 'src/none.csv'
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file_name)


def test_broken_csv():
    """Тестирование поврежденного файла"""
    file_name = 'tests/test_items.csv'
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(file_name)
