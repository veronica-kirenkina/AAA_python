import random
from typing import Callable
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


def log(params: str) -> Callable:
    """
    Декоратор логирует время исполнения функции.
    Принимает шаблон и выводит случайное значение.
    :param params: str
    :return: Callable
    """

    def decorator(func: Callable) -> Callable:
        nonlocal params
        if not isinstance(params, str):
            params = params.__name__ + ' - {}c!'
            print(params.format(random.randint(1, 10)))

        def wrapper(*args, **kwargs):
            print(params.format(random.randint(1, 10)))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log
def bake(pizza: Pizza):
    """Готовит пиццу"""


@log('🛵 доставили за {} минут!')
def deliver(pizza: Pizza):
    """Доставляет пиццу"""


@log('🏠 забрали за {} минут!')
def pickup(pizza: Pizza):
    """Самовывоз"""


if __name__ == '__main__':
    bake(Margherita())
    deliver(Hawaiian())
