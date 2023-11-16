class Pizza:
    """Базовый класс для всех видов пицц"""

    def __init__(self, size: str = 'L', name: str = None, extra_ingredients: list = []):
        if size not in ['L', 'XL']:
            raise ValueError("У нас нет пиццы такого размера. "
                             "Размер может быть только L или XL.")
        self.size = size
        self.name = name
        self.ingredients = ["tomato sauce", "mozzarella"]
        self.ingredients.extend(extra_ingredients)

    def dict(self) -> dict[str]:
        """
        Метод выводит рецепт в виде словаря
        :return: dict[str]
        """
        return {self.__dict__['name']: ', '.join(self.__dict__['ingredients'])}

    def __eq__(self, other) -> bool:
        """
        Метод позволяет сравнить две пиццы на равенство
        :param self: Pizza
        :param other: Pizza
        :return: bool
        """
        return self.ingredients == other.ingredients and self.size == other.size


class Margherita(Pizza):
    """Класс пиццы Маргарита"""

    def __init__(self, size: str = "L"):
        self.name = "Margherita 🧀"
        self.extra_ingredients = ["tomatoes"]
        super().__init__(size, self.name, self.extra_ingredients)


class Pepperoni(Pizza):
    """Класс пиццы Пепперони"""

    def __init__(self, size: str = "L"):
        self.name = "Pepperoni 🍕"
        self.extra_ingredients = ["pepperoni"]
        super().__init__(size, self.name, self.extra_ingredients)


class Hawaiian(Pizza):
    """Класс Гавайской пиццы"""

    def __init__(self, size: str = "L"):
        self.name = "Hawaiian 🍍"
        self.extra_ingredients = ["chicken", "pineapples"]
        super().__init__(size, self.name, self.extra_ingredients)
