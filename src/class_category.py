class Category:
    """Класс для представления категории"""
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = []  # Приватный атрибут для хранения списка товаров
        self.add_products(products)  # Используем метод для добавления товаров
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_products(self, products: list):
        """Метод для добавления товаров в категорию"""
        for product in products:
            self._products.append(product)

    def get_products(self):
        """Метод для получения списка товаров"""
        return self._products


# Пример использования:
category = Category("Электроника", "Технические устройства", [])
category.add_products(["Смартфон", "Планшет", "Ноутбук"])
print(category.get_products())
