import pytest
import random
from pizza import Pizza, Margherita, Pepperoni, Hawaiian
from services import bake, deliver, pickup
from cli import order, menu
from click.testing import CliRunner


def test_equality():
    """
    Проверка пицц на равенство/
    проверка корректность работы магического метода __eq__
    :return: None
    """
    assert Hawaiian() == Hawaiian()
    assert Hawaiian(size='XL') != Hawaiian(size='L')
    assert Hawaiian() != Pepperoni()


def test_pizza_dict():
    """
    Проверка на корректность работы функции dict
    :return: None
    """
    assert Pizza().dict() == {None: 'tomato sauce, mozzarella'}
    assert Margherita().dict() == {'Margherita 🧀': 'tomato sauce, mozzarella, tomatoes'}
    assert Pepperoni().dict() == {'Pepperoni 🍕': 'tomato sauce, mozzarella, pepperoni'}
    assert Hawaiian().dict() == {'Hawaiian 🍍': 'tomato sauce, mozzarella, chicken, pineapples'}
    assert Margherita().__class__.__name__ != str(*Hawaiian().dict().keys())


def test_size_exceptions():
    """
    Провека корректность вызова исключений при некорректном вводе размера пиццы
    :return: None
    """
    with pytest.raises(ValueError):
        Pizza(size='l')
    with pytest.raises(ValueError):
        Pizza(size=30)


def test_with_decorator():
    """
    Проверка выходов функций услуг
    :return: None
    """
    assert deliver(Margherita()) is None
    assert pickup(Margherita()) is None


def test_bake(capsys):
    """
    Проверка работы функции bake вместе с декоратором
    :return: None
    """
    random.seed(42)
    bake(Margherita())
    out = capsys.readouterr().out.split("\n")
    assert out[0] == 'bake - 2c!'


def test_deliver(capsys):
    """
    Проверка работы функции deliver вместе с декоратором
    :return: None
    """
    result = deliver(Margherita())
    out, err = capsys.readouterr().out.split("\n")
    assert result is None
    assert out.startswith("🛵 доставили за")


def test_pickup(capsys):
    """
    Проверка работы функции pickup вместе с декоратором
    :return: None
    """
    result = pickup(Margherita())
    out, err = capsys.readouterr().out.split("\n")
    assert result is None
    assert out.startswith("🏠 забрали за")


def test_menu():
    """
    Проверка корректности выводимого меню
    :return: None
    """
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.output == "- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n" \
                            "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n" \
                            "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n"


def test_invalid_order():
    """
    Проверка работы терминальных функций при некорректном наименовании пиццы
    :return: None
    """
    runner = CliRunner()
    result = runner.invoke(order, ["margarita"])
    assert result.output.strip() == ''


def test_order_no_delivery_flag():
    """
    Проверка работы терминальных функций заказа без использования флага доставки
    :return: None
    """
    runner = CliRunner()
    result = runner.invoke(order, ["pepperoni"])
    assert " забрали за" in result.output.strip()


def test_order_no_delivery_flag():
    """
    Проверка работы терминальных функций заказа с использованием флага доставки
    :return: None
    """
    runner = CliRunner()
    result = runner.invoke(order, ["pepperoni", "--delivery"])
    assert " доставили за" in result.output.strip()
