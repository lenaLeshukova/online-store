import pytest

from src.models import Product, Category


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
