class Product:
    """ Класс для предоставления товара"""
    name: str
    description: str
    _price: float
    quantity_stock: int

    def __init__(self, name: str, description: str, price: float, quantity_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock

    @property
    def price(self):
        """Геттер для атрибута цены"""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для атрибута цены"""
        if value <= 0:
            print("Ошибка: Цена введена некорректно.")
        else:
            self._price = value

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity_stock: int):
        """Метод класса для создания объекта товара"""
        return cls(name, description, price, quantity_stock)
