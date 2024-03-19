from src.class_category import Category


def test_category_creation():
    copy_1 = Category('fruits', "Fruits from Russia", ['apples', 'pears', 'Oranges'])
    copy_2 = Category('berries', "Berries from Russia", ['cherry', 'raspberries', 'strawberry', 'watermelon'])

    assert copy_1
    assert copy_2


def test_category_products():
    copy_2 = Category('berries', "Berries from Russia", ['cherry', 'raspberries', 'strawberry', 'watermelon'])

    assert copy_2.products == ['cherry', 'raspberries', 'strawberry', 'watermelon']


def test_total_categories():
    initial_total_categories = Category.total_categories

    Category('fruits', "Fruits from Russia", ['apples', 'pears', 'Oranges'])
    Category('berries', "Berries from Russia", ['cherry', 'raspberries', 'strawberry', 'watermelon'])

    assert Category.total_categories == initial_total_categories + 2


def test_total_products():
    initial_total_products = Category.total_products

    Category('fruits', "Fruits from Russia", ['apples', 'pears', 'Oranges'])
    Category('berries', "Berries from Russia", ['cherry', 'raspberries', 'strawberry', 'watermelon'])

    assert Category.total_products == initial_total_products + 7
