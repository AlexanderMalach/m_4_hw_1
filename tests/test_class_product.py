import pytest

from src.class_product import Product, Smartphone, Grass


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 10.0, 100)


@pytest.fixture
def smartphone_product():
    return Smartphone("Test Product2", "Test Description2", 20.0, 200, 1000, "USSR-fon - 20", 256, "red")


@pytest.fixture
def grass_product():
    return Grass("Test Product2", "Test Description2", 20.0, 200, "Russian", 10,  "red")


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
    assert smartphone_product.storage_capacity == 256
    assert smartphone_product.color == "red"


def test_add_method_smartphone(smartphone_product):
    other_product = Smartphone("Test Product2", "Test Description2", 20.0, 200, 1000, "USSR-fon - 20", 256, "red")
    total_price = smartphone_product + other_product
    assert total_price == 8000.0


def test_add_smartphone_and_product(smartphone_product):
    other_product = Product("Other Product", "Other Description", 15.0, 50)
    assert smartphone_product + other_product is TypeError


def test_create_grass(grass_product):
    assert grass_product.name == "Test Product2"
    assert grass_product.description == "Test Description2"
    assert grass_product.price == 20.0
    assert grass_product.quantity == 200
    assert grass_product.country == "Russian"
    assert grass_product.germination_period == 10
    assert grass_product.color == "red"


def test_add_method_grass(grass_product):
    other_product = Grass("Test Product2", "Test Description2", 20.0, 200, "Russian", 10,  "red")
    total_price = grass_product + other_product
    assert total_price == 8000.0


def test_add_grass_and_product(grass_product):
    other_product = Product("Other Product", "Other Description", 15.0, 50)
    assert grass_product + other_product is TypeError
