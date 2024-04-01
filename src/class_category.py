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

    def add_products(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    def __len__(self) -> int():
        return len(self.__products)

    def __str__(self):
        """Метод для вывода информации о товарах"""
        return f"{self.name}, количество продуктов: {len(self)} шт."



z = Category('apple', 'red', ['1', '2', '3'])
print(len(z))
print((z))