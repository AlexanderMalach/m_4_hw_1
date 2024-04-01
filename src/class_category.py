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

    def add_products(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    def __len__(self) -> int():
        return self.__products

    def __str__(self) -> list[str]:
        """Метод для вывода информации о товарах"""
        list_info = []
        for product in self.__products:
            list_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_stock} шт.")
        return list_info
