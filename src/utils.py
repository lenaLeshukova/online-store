import json
import os

from src.models import Category, Product


def load_data_from_json(file_path: str) -> list[Category]:
    """Загружает данные из JSON и преобразует их в объекты классов
    Category и Product"""

    # Исправляем путь, если запускаем из разных папок
    full_path = os.path.abspath(file_path)

    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        products_list = []

        # Сначала создаем объекты товаров для этой категории
        for product_data in category_data.get('products', []):
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products_list.append(product)

        # Создаем объект категории и добавляем список товаров
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products_list
        )
        categories.append(category)

    return categories
