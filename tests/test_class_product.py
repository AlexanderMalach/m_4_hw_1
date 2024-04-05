import pytest

from src.class_product import Product, Smartphone, Grass


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 10.0, 100)


@pytest.fixture
def smartphone_product():
    return Smartphone("Test Product2", "Test Description2", 20.0, 200, 1000, "USSR-fon - 20", 256, "red")


def test_create_product(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 10.0
    assert sample_product.quantity == 100


def test_price_getter_and_setter(sample_product):
    sample_product.price = 20.0
    assert sample_product.price == 20.0


def test_add_method(sample_product):
    other_product = Product("Other Product", "Other Description", 15.0, 50)
    total_price = sample_product + other_product
    assert total_price == 1750.0


def test_crete_smartphone(smartphone_product):
    assert smartphone_product.name == "Test Product2"
    assert smartphone_product.description == "Test Description2"
    assert smartphone_product.price == 20.0
    assert smartphone_product.quantity == 200
    assert smartphone_product.performance == 1000.0
    assert smartphone_product.model == "USSR-fon - 20"
    assert smartphone_product.pmc == 256
    assert smartphone_product.color == "red"

def test_add_method_smartphone(sample_product, smartphone_product):
    other_product = sample_product
    other_smartphone = smartphone_product
    total_price = other_product + other_smartphone
    assert total_price is TypeError
