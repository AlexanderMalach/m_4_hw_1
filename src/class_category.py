class Category:
    """Класс для представления категории"""
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения списка товаров
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_products(self, product: list):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)

    @property
    def product_info(self, price: float, quantity_stock: int):
        """Геттер для вывода информации о товарах"""
        list_info = []
        for product in self.__products:
            list_info.append(f"{product}, {price} руб. Остаток: {quantity_stock} шт.")
        return list_info

