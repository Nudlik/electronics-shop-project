import csv
import os

from settings import CSV_PATH


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
        self.price = self.__validate_data(price)
        self.quantity = self.__validate_data(quantity)

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = self.__validate_name(name)

    @classmethod
    def __validate_name(cls, name: str) -> str:
        """
        Валидация имени товара не более 10 символов.

        :param name: Наименование товара
        :return: Обрезанное наименование товара
        """
        if len(name) > 10:
            return name[:10]
        return name

    @classmethod
    def __validate_data(cls, data: int | float | str) -> int | float:
        """
        Валидация данных для полей экземпляра класса.

        :param data: Принимает данные типа int | float | str
        :return: Преобразованные данные
        """
        if not (isinstance(data, int | float | str) or str(data).isdigit()):
            raise ValueError('Неверный тип данных')
        elif isinstance(data, str | float):
            if data.count('.') == 1 or type(data) == float:
                return float(data)
            return int(data)

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        и очищает текущие экземляры хранящиеся в all.

        :return: None
        """
        if not os.path.exists(CSV_PATH):
            raise FileNotFoundError(f'Отсутствует csv-файл по пути {CSV_PATH}')
        with open(CSV_PATH) as file:
            reader: csv.DictReader = csv.DictReader(file)
            cls.all.clear()
            [cls(**row) for row in reader]

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки.

        :param string: числовая строка
        :return: целое число
        """
        if not (isinstance(string, int | float | str) or string.isdigit()):
            raise ValueError('Неверный тип данных')
        return int(float(string))

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
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f'{__class__.__name__}(name="{self.__name}", price="{self.price}", quantity="{self.quantity}")'
