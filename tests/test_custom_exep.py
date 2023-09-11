""" Тест кастомных исключений """
import pytest

from src.custom_exep import InstantiateCSVError


def test_InstantiateCSVError():
    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError


def test_InstantiateCSVError_msg():
    ex = InstantiateCSVError()
    assert ex.message == 'Файл item.csv поврежден'
    ex = InstantiateCSVError('abracadabra')
    assert ex.message == 'abracadabra'
