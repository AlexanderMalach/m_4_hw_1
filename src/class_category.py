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

    def add_products(self, products: list):
        """Метод для добавления товаров в категорию"""
        for product in products:
            self.__products.append(product)

    def get_products(self):
        """Метод для получения списка товаров"""
        return self.__products

    @property
    def products(self, price: float, quantity_stock: int):
        """Геттер для вывода информации о товарах"""
        for product in self.__products:
            print(f"{product}, {price} руб. Остаток: {quantity_stock} шт.")

