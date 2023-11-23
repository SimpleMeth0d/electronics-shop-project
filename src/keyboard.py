from src.item import Item


class Mixin:
    __language = 'EN'

    def __init__(self):
        self.__language = 'EN'

    def __str__(self):
        return f'{self.language}'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Mixin):
    pass
