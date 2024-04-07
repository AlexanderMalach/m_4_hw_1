from abc import ABC, abstractmethod


class AbsProduct(ABC):

    @abstractmethod
    def __init__(self):
        # super().__init__()
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class CreationInfoMixin:
    """Миксин для вывода информации о создании объекта"""

    def __init__(self):
        super().__init__()
        print(repr(self))

    def __repr__(self):
        return (f"Создан объект класса {self.__class__.__name__}: "
                f"{', '.join([f"{key}: {value}" for key, value in self.__dict__.items()])}")


class Product(AbsProduct, CreationInfoMixin):
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
        CreationInfoMixin.__init__(self)

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
        if quantity == 0:
            return cls(name, description, price, quantity)
        else:
            raise ValueError

    def __str__(self) -> str:
        """Метод для вывода информации о товаре"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) != type(self):
            return TypeError
        else:
            return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """ Класс для предоставления смартфонов"""

    def __init__(self, name: str, description: str, price: float, quantity: int, performance: float, model: str,
                 storage_capacity: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            return TypeError
        else:
            return self.price * self.quantity + other.price * other.quantity


class Grass(Product):
    """ Класс для предоставления газонной травы"""

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if not isinstance(other, Grass):
            return TypeError
        else:
            return self.price * self.quantity + other.price * other.quantity


product1 = Product('Продукт1', 'Описание продукта', 1200, 10)
smartphone1 = Smartphone('Смартфон1', 'Описание смартфона', 1000, 5, 2.3, 'Модель1', 64, 'Черный')
grass1 = Grass('Трава1', 'Описание травы', 500, 20, 'Страна1', 14, 'Зеленый')
print(Product.__mro__)
