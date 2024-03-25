import pytest

from src.class_product import Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 10.0, 100)


def test_product_creation(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 10.0
    assert sample_product.quantity_stock == 100


def test_set_price(sample_product):
    sample_product.price = 20.0
    assert sample_product.price == 20.0


def test_set_price_negative(sample_product):
    sample_product.price = -10.0
    assert sample_product.price == 10.0  # Проверяем, что цена осталась прежней
