import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def sample_category():
    products = [Product("Product 1", "Description 1", 10.0, 100), Product("Product 2", "Description 2", 20.0, 50)]
    return Category("Test Category", "Test Description", products)


def test_category_creation(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category._Category__products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_product_info(sample_category):
    expected_info = ["Product 1, 10.0 руб. Остаток: 100 шт.", "Product 2, 20.0 руб. Остаток: 50 шт."]
    assert sample_category.product_info() == expected_info
