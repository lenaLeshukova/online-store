from src.models import Product, Category


def test_product_init(product_iphone):
    """Тест корректности инициализации товара"""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_category_init(category_smartphones):
    """Тест корректности инициализации категории"""
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Описание"
    assert len(category_smartphones.products) == 1


def test_category_counts():
    """Тест подсчета количества категорий и продуктов"""
    # Сбрасываем счетчики для чистоты теста
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Оп", 100, 1)
    p2 = Product("Товар 2", "Оп", 200, 2)

    cat1 = Category("Кат 1", "Оп", [p1])
    assert Category.category_count == 1
    assert Category.product_count == 1

    cat2 = Category("Кат 2", "Оп", [p1, p2])
    assert Category.category_count == 2
    assert Category.product_count == 3  # 1 (из первой) + 2 (из второй)
