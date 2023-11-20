from src.item import Item
from src.phone import Phone


phone1 = Phone("iPhone 14", 120000, 5, 2)
item1 = Item("Смартфон", 10000, 20)


def test_str():
    """
    Тестирует метод str
    """
    assert str(phone1) == 'iPhone 14'


def test_repr():
    """
    Тестирует метод repr
    """
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    assert phone1.number_of_sim == 2


def test_add():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10