import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def sample_category():
    products = [Product("Product 1", "Description 1", 10.0, 100), Product("Product 2", "Description 2", 15.0, 50)]
    return Category("Test Category", "Test Description", products)


def test_create_category(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category) == 150


def test_add_products(sample_category):
    new_product = Product("New Product", "New Description", 20.0, 75)
    sample_category.add_products(new_product)
    assert len(sample_category) == 225
    assert sample_category.total_products == 3


def test_category_length(sample_category):
    assert len(sample_category) == 150
