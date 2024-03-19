from src.class_product import Product


def test_product_creation():
    test_name = 'Fuji'
    test_description = 'The apples have yellowish skin and orange-red stripes and are round in shape'
    test_price = 30.5
    test_quantity_stock = 300

    copy = Product(test_name, test_description, price=test_price, quantity_stock=test_quantity_stock)

    assert copy


def test_product_attributes():
    test_name = 'Fuji'
    test_description = 'The apples have yellowish skin and orange-red stripes and are round in shape'
    test_price = 30.5
    test_quantity_stock = 300

    copy = Product(test_name, test_description, price=test_price, quantity_stock=test_quantity_stock)

    assert copy.name == 'Fuji'
    assert isinstance(copy.name, str)
    assert copy.description == 'The apples have yellowish skin and orange-red stripes and are round in shape'
    assert isinstance(copy.description, str)
    assert copy.price == 30.5
    assert isinstance(copy.price, float)
    assert copy.quantity_stock == 300
    assert isinstance(copy.quantity_stock, int)
