from src.keyboard import Keyboard

kb1 = Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    """
    Тестирует метод str
    """
    assert str(kb1) == "Dark Project KD87A"


def test_language():
    assert str(kb1.language) == "EN"
    kb1.change_lang()
    assert str(kb1.language) == "RU"
    kb1.change_lang()
    assert str(kb1.language) == "EN"
    