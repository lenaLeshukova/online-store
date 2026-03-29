from typing import Any

import pytest

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


def test_smartphone_init(smartphone_iphone: Any) -> None:
    """Тест инициализации смартфона и его уникальных атрибутов"""
    assert smartphone_iphone.name == "Iphone 15"
    assert smartphone_iphone.efficiency == 98.2
    assert smartphone_iphone.model == "15"
    assert smartphone_iphone.memory == 512


def test_grass_init(grass_green: Any) -> None:
    """Тест инициализации травы и её уникальных атрибутов"""
    assert grass_green.name == "Газон"
    assert grass_green.country == "Россия"
    assert grass_green.germination_period == "7 дней"


def test_products_addition(smartphone_iphone: Any,
                           smartphone_samsung: Any) -> None:
    """Тест сложения двух смартфонов (одинаковый класс)"""
    # (210000 * 8) + (100000 * 2) = 1 680 000 + 200 000 = 1 880 000
    assert smartphone_iphone + smartphone_samsung == 1880000.0


def test_products_addition_error(smartphone_iphone: Any,
                                 grass_green: Any) -> None:
    """Тест ошибки при сложении разных классов """
    with pytest.raises(TypeError):
        smartphone_iphone + grass_green


def test_add_product_validation(category_smartphones: Any) -> None:
    """Тест защиты метода add_product от некорректных типов """
    # Попытка добавить строку вместо объекта Product
    with pytest.raises(TypeError):
        category_smartphones.add_product("Не товар, а строка")

    # Попытка добавить число
    with pytest.raises(TypeError):
        category_smartphones.add_product(12345)


def test_add_subclass_product(category_smartphones: Any,
                              grass_green: Any) -> None:
    """Тест, что наследники Product (LawnGrass) добавляются успешно"""
    initial_count = Category.product_count
    category_smartphones.add_product(grass_green)
    assert Category.product_count == initial_count + 1
    assert "Газон" in category_smartphones.products


def test_product_price_setter_confirm(product_iphone: Any,
                                      monkeypatch: Any) -> None:
    """Тест сеттера цены с подтверждением понижения (через input)"""
    # monkeypatch — это встроенная фикстура в pytest, позволяет имитировать
    # ввод с помощью лямбды функции (импут).
    # Имитируем ввод пользователя 'y' (согласие на понижение)
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product_iphone.price = 150000.0
    assert product_iphone.price == 150000.0

    # Имитируем ввод 'n' (отказ от понижения)
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product_iphone.price = 100000.0
    assert product_iphone.price == 150000.0  # Цена осталась старой
