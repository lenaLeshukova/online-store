from typing import Any

from src.models import Product, Category


def test_product_init(product_iphone: Any) -> None:
    """Тест корректности инициализации товара и работы геттера цены"""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_product_price_setter(product_iphone: Any) -> None:
    """Тест сеттера цены (валидация и уменьшение)"""
    # Проверка некорректной цены (не должна измениться)
    product_iphone.price = -10
    assert product_iphone.price == 210000.0

    # В тесте проверяем, что цена меняется при валидном значении
    product_iphone.price = 250000.0
    assert product_iphone.price == 250000.0


def test_category_init(category_smartphones: Any) -> None:
    """Тест инициализации категории и приватного атрибута"""
    assert category_smartphones.name == "Смартфоны"
    # category.products возвращает строку (по заданию)
    assert "Iphone 15" in category_smartphones.products


def test_add_product(category_smartphones: Any) -> None:
    """Тест добавления продукта через метод add_product"""
    new_p = Product("Nokia", "Old", 1000.0, 10)
    category_smartphones.add_product(new_p)
    assert "Nokia" in category_smartphones.products


def test_new_product_classmethod() -> None:
    """Тест логики объединения дублей """
    p1 = Product("Samsung", "Note 1", 100.0, 5)
    products_list = [p1]

    # Данные для "такого же" товара, но дороже и в другом количестве
    new_data = {
        "name": "Samsung",
        "description": "Note 2",
        "price": 150.0,
        "quantity": 10
    }

    updated_p = Product.new_product(new_data, products_list)

    assert updated_p.name == "Samsung"
    assert updated_p.quantity == 15  # 5 + 10
    assert updated_p.price == 150.0  # Выбрана максимальная цена


def test_category_counts_reset() -> None:
    """Тест корректности счетчиков классов"""
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Т1", "Д", 100, 1)
    cat1 = Category("С1", "Д", [p1])

    assert Category.category_count == 1
    assert Category.product_count == 1

    p2 = Product("Т2", "Д", 200, 2)
    cat1.add_product(p2)

    assert Category.product_count == 2
