from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса Phone, дочернего от класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт.
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        """Проверяет, является ли новое значение целым и положительным числом"""
        if not isinstance(num, int) or num <= 0 or not isinstance(num, int) and num <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = num
