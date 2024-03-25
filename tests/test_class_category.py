import pytest

from src.class_category import Category


@pytest.fixture
def filled_category():
    return Category("Filled Category", "Has description", ["Product 1", "Product 2"])


def test_add_products(empty_category):
    empty_category.add_products(["Product A", "Product B"])
    assert empty_category.get_products() == ["Product A", "Product B"]


def test_get_products(filled_category):
    assert filled_category.get_products() == ["Product 1", "Product 2"]


def test_total_categories():
    assert Category.total_categories == 2

def test_total_products(filled_category):
    assert Category.total_products == 5


def test_products_info(filled_category):
    expected_output = "Product 1, 80 руб. Остаток: 15 шт.\nProduct 2, 80 руб. Остаток: 15 шт.\n"
    assert filled_category.products_info() == expected_output


if __name__ == "__main__":
    pytest.main()
