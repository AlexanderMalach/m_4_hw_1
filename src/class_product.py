class Product:
    """ Класс для предоставления товара"""
    name: str
    description: str
    price: float
    quantity_stock: int

    def __init__(self, name: str, description: str, price: float, quantity_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock

