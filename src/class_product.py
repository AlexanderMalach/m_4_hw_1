class Product:
    """ Класс для предоставления товара"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для атрибута цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для атрибута цены"""
        if value <= 0:
            print("Ошибка: Цена введена некорректно.")
        else:
            self.__price = value

    @classmethod
    def create_product(cls, dict_info: dict):
        """Метод класса для создания объекта товара"""
        name = dict_info['name']
        description = dict_info['description']
        price = dict_info['price']
        quantity = dict_info['quantity']
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        """Метод для вывода информации о товаре"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(type(other), ):
            return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, performance: float, model: str,
                 pmc: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.pmc = pmc
        self.color = color


class Grass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, manufacturer_country: str,
                 germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
