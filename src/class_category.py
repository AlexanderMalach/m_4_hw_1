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
        Category.total_products += len(products)

    def add_products(self, product: str):
        """Метод для добавления товаров в категорию"""
        return self.__products.append(product)

    @property
    def product_info(self):
        """Метод для вывода информации о товарах"""
        list_info = []
        for product in self.__products:
            list_info.append(f"{Product.name}, {Product.price} руб. Остаток: {Product.quantity_stock} шт.")
        return list_info
