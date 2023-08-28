"""Здесь надо написать тесты с использованием pytest для модуля item."""
from unittest.mock import patch

import pytest

from src.item import Item


@pytest.mark.parametrize('name, price, quantity, expected', [
    ('Смартфон', 10000, 20, 200000),
    ('Ноутбук', 20000, 5, 100000)
])
def test_item_calculate_total_price(name, price, quantity, expected):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == expected


@pytest.mark.parametrize('name, price, quantity, pay_rate, expected', [
    ('Смартфон', 10000, 20, 0.8, 8000.0),
    ('Ноутбук', 20000, 5, 0.8, 16000.0)
])
def test_item_apply_discount(name, price, quantity, pay_rate, expected):
    item = Item(name, price, quantity)
    item.pay_rate = pay_rate
    item.apply_discount()
    assert item.price == expected


def test_item_all():
    Item.all.clear()
    item_1 = Item('Смартфон', 10000, 20)
    item_2 = Item('Ноутбук', 20000, 5)
    assert len(Item.all) == 2
    assert Item.all == [item_1, item_2]


def test_item_property_name():
    item_1 = Item('', 0, 0)
    item_1.name = '1234567891011'
    assert item_1.name == '1234567891'
    item_1.name = '1'
    assert item_1.name == '1'


@pytest.mark.parametrize('num, expected', [
    (20, 20),
    ('20', 20),
    (20.0, 20),
    ('20.0', 20)
])
def test_item__validate_data(num, expected):
    assert Item._Item__validate_data(num) == expected


@pytest.mark.parametrize('any_, expected', [
    ([20], ValueError),
    ({20: 20}, ValueError),
    (set('20'), ValueError),
    ((20,), ValueError)
])
def test_item__validate_data_raise(any_, expected):
    with pytest.raises(expected):
        Item._Item__validate_data(any)


@pytest.mark.parametrize('num, expected', [
    ('20', 20),
    ('20.0', 20),
    ('2.00', 2),
    ('2', 2)
])
def test_item_string_to_number(num, expected):
    assert Item.string_to_number(num) == expected


@pytest.mark.parametrize('any_str, expected', [
    (20, ValueError),
    ({20: 20}, ValueError),
    (set('20'), ValueError),
    ((20,), ValueError)
])
def test_item_string_to_number_raise(any_str, expected):
    with pytest.raises(expected):
        Item.string_to_number(any_str)


def test_item_instantiate_from_csv():
    assert Item.instantiate_from_csv() is None


@pytest.mark.parametrize('name, price, quantity, expected', [
    ('Смартфон', 10000, 20, "Item('Смартфон', 10000, 20)"),
    ('Ноутбук', 20000, 5, "Item('Ноутбук', 20000, 5)")
])
def test_item__repr__(name, price, quantity, expected):
    item = Item(name, price, quantity)
    assert item.__repr__() == expected


@patch('src.item.CSV_PATH', 'FileNotFoundError.py')
def test_item_instantiate_from_csv1():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


@pytest.mark.parametrize('name, price, quantity, expected', [
    ('Смартфон', 0, 0, 'Смартфон'),
    ('Ноутбук', 0, 0, 'Ноутбук')
])
def test_item__str__(name, price, quantity, expected):
    item = Item(name, price, quantity)
    assert item.__str__() == expected
