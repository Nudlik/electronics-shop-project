"""тесты с использованием pytest для модуля keyboard."""
import pytest

from src.keyboard import Keyboard


@pytest.fixture
def test_fixture_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_representation(test_fixture_keyboard):
    assert str(test_fixture_keyboard) == 'Dark Project KD87A'


def test_keyboard_change_lang(test_fixture_keyboard):
    assert test_fixture_keyboard.language == 'EN'
    test_fixture_keyboard.change_lang()
    assert test_fixture_keyboard.language == 'RU'


def test_keyboard_language_error(test_fixture_keyboard):
    with pytest.raises(AttributeError):
        test_fixture_keyboard.language = 'CH'
