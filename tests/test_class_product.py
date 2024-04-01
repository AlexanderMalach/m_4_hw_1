import pytest

from src.class_product import Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 10.0, 100)


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
