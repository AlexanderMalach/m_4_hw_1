from src.class_product import Product


class Category:
    """Класс для представления категории"""
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_products = len(self.__products)

    def add_products(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    def __len__(self) -> int():
        return len(self.__products)

    def __str__(self):
        """Метод для вывода информации о товарах"""
        total_product = 0
        for i in self.__products:
            total_product += Product.quantity
        return f"{self.name}, количество продуктов: {total_product} шт."
