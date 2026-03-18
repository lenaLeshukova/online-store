import json

from src.models import Category, Product
from src.utils import load_data_from_json


def test_load_data_from_json(tmp_path):
    """Тест корректности загрузки данных из JSON и создания объектов"""

    # 1. Создаем временный файл с тестовыми данными
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Тестовое описание",
            "products": [
                {
                    "name": "Samsung",
                    "description": "256GB",
                    "price": 100000.0,
                    "quantity": 5
                }
            ]
        }
    ]

    # tmp_path — это встроенная фикстура pytest для создания временных папок
    temp_file = tmp_path / "test_products.json"
    temp_file.write_text(json.dumps(test_data), encoding='utf-8')

    # 2. Вызываем функцию загрузки
    categories = load_data_from_json(str(temp_file))

    # 3. Проверяем результат
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"

    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Samsung"
    assert categories[0].products[0].price == 100000.0
