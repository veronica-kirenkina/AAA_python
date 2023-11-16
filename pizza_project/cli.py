import click
from services import bake, deliver, pickup
from pizza import Pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Функция позволяет через терминал осуществить приготовление и доставку пиццы
    с указанием временных затрат на каждом этапе
    :param pizza: str
    :param delivery: bool
    :return: None
    """
    for pizza_name in Pizza.__subclasses__():
        if pizza_name().__class__.__name__.lower() == pizza:
            bake(pizza_name())
            if delivery:
                deliver(pizza_name())
            else:
                pickup(pizza_name())


@cli.command()
def menu() -> None:
    """
    Функция позволяет через терминал осуществить посмотреть на меню
    :return: None
    """
    for pizza in Pizza.__subclasses__():
        recipe = pizza().dict()
        print('- ', *recipe.keys(), ': ', *recipe.values(), sep='')


if __name__ == '__main__':
    cli()
