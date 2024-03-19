class Category:
    """  Класс для предоставления категории"""
    name: str
    description: str
    products: list
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_products += len(self.products)
