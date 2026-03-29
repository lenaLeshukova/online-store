import pytest

from src.models import Product, Smartphone, LawnGrass, Category


# Фикстуры классы

@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_smartphones(product_iphone):
    # Сбрасываем счетчики перед тестом, чтобы они были чистыми
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Описание", [product_iphone])


# Фикстуры наследование
@pytest.fixture
def smartphone_iphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2,
                      "15", 512, "Gray space")


@pytest.fixture
def smartphone_samsung():
    return Smartphone("Samsung Galaxy S23", "256GB", 100000.0, 2, 95.5, "S23",
                      256, "Black")


@pytest.fixture
def grass_green():
    return LawnGrass("Газон", "Зеленая", 500.0, 20, "Россия", "7 дней",
                     "Зеленый")
