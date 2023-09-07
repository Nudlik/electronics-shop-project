from src.item import Item


class MixinKeyboard:

    def __init__(self, language: str = 'EN'):
        self._language: str = language

    def change_lang(self):
        match self.language:
            case 'EN':
                self._language = 'RU'
            case 'RU':
                self._language = 'EN'
        return self

    @property
    def language(self):
        return self._language


class Keyboard(Item, MixinKeyboard):

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(name, price, quantity)
        MixinKeyboard.__init__(self, language)

        self.all.append(self)
