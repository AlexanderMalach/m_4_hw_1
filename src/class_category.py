from src.class_product import Product, Smartphone, Grass


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
        if product.quantity !=0:
            if isinstance(product, (Product, Smartphone, Grass)):
                self.__products.append(product)
                Category.total_products += 1
            else:
                return TypeError
        raise ValueError("Товар с нулевым количеством добавить нельзя!")
    def __len__(self):
        total_product = 0
        for i in self.__products:
            total_product += i.quantity
        return total_product

    def __str__(self) -> str:
        """Метод для вывода информации о товарах"""

        return f"{self.name}, количество продуктов: {len(self)} шт."
