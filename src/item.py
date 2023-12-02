import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return f"Файл items.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all = self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты класса Item и дочерних классы')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        Осуществляется проверка длины наименования товара. (10 символов)
        Если наименование длинее 10 символов, сокращается до 10 символов.
        """
        self.__name = new_name
        if len(list(self.__name)) > 10:
            self.__name = str("".join(list(self.__name)[:9]))
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename='src/items.csv'):
        '''
        Класс-метод, инициализирующий экземпляры класса "Item"
        данными из файла src/items.csv
        '''
        path = os.path.join(os.path.dirname(__file__), '..', filename)

        try:
            with open(path, 'r', encoding='windows-1251', newline='') as csvfile:
                Item.all.clear()
                reader = csv.DictReader(csvfile, delimiter=',')
                dict_reader = list(reader)
                for row in dict_reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')
        except (KeyError, ValueError):
            raise InstantiateCSVError()

    @staticmethod
    def string_to_number(string):
        '''
        Статический метод, возвращающий число из числа-строки
        '''
        return int(float(string))
