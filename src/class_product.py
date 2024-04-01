class Product:
    """ Класс для предоставления товара"""
    name: str
    description: str
    __price: float
    quantity_stock: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_stock = quantity

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

    def __str__(self) -> list[str]:
        """Метод для вывода информации о товарах"""
        list_info = []
        for product in self.__products:
            list_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_stock} шт.")
        return list_info
