from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = self.__validate_sim(number_of_sim)

        super().all.append(self)

    def __repr__(self):
        return f'{__class__.__name__}(' + super().__repr__().split('(')[1][:-1] + f', {self.__number_of_sim})'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim: int):
        self.__number_of_sim = self.__validate_sim(count_sim)

    @staticmethod
    def __validate_sim(sim: int) -> int:
        if sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        return sim
