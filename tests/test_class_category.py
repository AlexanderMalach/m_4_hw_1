from src.class_category import Category


def test_category_creation():
    category = Category("Электроника", "Товары в категории электроники", ["Телефон", "Планшет"])
    assert category.name == "Электроника"
    assert category.description == "Товары в категории электроники"
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_add_products():
    category = Category("Электроника", "Товары в категории электроники", [])
    category.add_products(["Телефон", "Планшет"])
    assert len(category.__products) == 2

def test_product_info():
    category = Category("Электроника", "Товары в категории электроники", ["Телефон", "Планшет"])
    product_info = category.product_info(1000, 10)
    assert len(product_info) == 2
    assert product_info[0] == "Телефон, 1000 руб. Остаток: 10 шт."
    assert product_info[1] == "Планшет, 1000 руб. Остаток: 10 шт."

