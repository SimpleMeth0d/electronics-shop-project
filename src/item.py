import csv
import os


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all = self.all.append(self)

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
    def instantiate_from_csv(cls, filename):
        '''
        Класс-метод, инициализирующий экземпляры класса "Item"
        данными из файла src/items.csv
        '''
        path = os.path.join(os.path.dirname(__file__), '..', filename)
        with open(path, 'r', encoding='windows-1251', newline='') as csvfile:
            cls.all.clear()
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        '''
        Статический метод, возвращающий число из числа-строки
        '''
        return int(float(string))
