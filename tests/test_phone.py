"""тесты с использованием pytest для модуля phone."""
from src.phone import Phone
import pytest


@pytest.fixture
def test_fixture_phone():
    return Phone('iPhone 14', 120_000, 5, 2)


def test_phone_representation(test_fixture_phone):
    assert str(test_fixture_phone) == 'iPhone 14'
    assert repr(test_fixture_phone) == "Phone('iPhone 14', 120000, 5, 2)"


@pytest.mark.parametrize('number_of_sim, expected', [
    (0, ValueError),
    (-1, ValueError)
])
def test_phone_number_of_sim(test_fixture_phone, number_of_sim, expected):
    with pytest.raises(expected):
        test_fixture_phone.number_of_sim = number_of_sim


@pytest.mark.parametrize('number_of_sim, expected', [
    (3, 3),
    (4, 4)
])
def test_phone_number_of_sim_setter(number_of_sim, expected, test_fixture_phone):
    test_fixture_phone.number_of_sim = number_of_sim
    assert test_fixture_phone.number_of_sim == expected
