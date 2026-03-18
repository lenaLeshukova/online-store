class Product:
    """Класс для представления товара"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров"""
    name: str
    description: str
    products: list

    # Атрибуты класса для хранения счетчиков
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # При создании новой категории увеличиваем счетчик категорий на 1
        Category.category_count += 1

        # Прибавляем количество товаров в текущей категории к общему счетчику
        Category.product_count += len(self.products)
