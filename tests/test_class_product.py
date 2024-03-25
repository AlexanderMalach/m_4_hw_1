import pytest

from src.class_product import Product


@pytest.fixture
def product():
    return Product("Телефон", "Смартфон", 1000.0, 10)


def test_create_product():
    p = Product.create_product("Ноутбук", "Мощный ноутбук", 1500.0, 5)
    assert isinstance(p, Product)
    assert p.name == "Ноутбук"
    assert p.description == "Мощный ноутбук"
    assert p.price == 1500.0
    assert p.quantity_stock == 5


def test_price_setter_valid(product):
    product.price = 1200.0
    assert product.price == 1200.0


def test_price_setter_invalid(product, capsys):
    product.price = -500.0
    assert product.price == 1000.0  # Устанавливается старое значение цены из-за некорректного ввода
    captured = capsys.readouterr()
    assert "Ошибка: Цена введена некорректно." in captured.out


if __name__ == "__main__":
    pytest.main()
