"""Здесь надо написать тесты с использованием pytest для модуля item."""
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
    item_1 = Item('Смартфон', 10000, 20)
    item_2 = Item('Ноутбук', 20000, 5)
    assert len(Item.all) == 2
    assert Item.all == [item_1, item_2]
