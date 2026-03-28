from typing import Any


class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое отображение продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Сложение товаров (цена * количество + цена * количество)"""
        if isinstance(other, Product):
            return (self.price * self.quantity) + (
                    other.price * other.quantity)
        raise TypeError("Складывать можно только объекты класса Product")

    @classmethod
    def new_product(cls, product_data: dict,
                    products_list: list["Product"] | None = None) -> "Product":
        """Создание объекта из словаря с проверкой дублей"""
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        if products_list:
            for product in products_list:
                if product.name == name:
                    # Складываем количество
                    product.quantity += quantity
                    # Выбираем максимальную цену
                    product.price = max(product.price, price)
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с валидацией и подтверждением снижения"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            user_answer = input(
                f"Вы уверены, что хотите снизить цену с {self.__price} "
                f"до {new_price}? (y/n): ")
            if user_answer.lower() != 'y':
                print("Действие отменено.")
                return

        self.__price = new_price


class Category:
    """Класс для представления категории товаров"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str,
                 products: list | None = None) -> None:
        self.name = name
        self.description = description
        # Приватный атрибут списка товаров
        self.__products: list[Product] = []

        Category.category_count += 1

        # Наполняем список через метод add_product
        if products:
            for product in products:
                self.add_product(product)

    def __str__(self) -> str:
        """Строковое отображение категории с подсчетом всех штук на складе"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Any) -> None:
        """Метод добавляет продукт в список. Ничего не возвращает"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> str:
        """Оптимиз. геттер: использует __str__ каждого продукта,
        возвращает строковое представление списка товаров"""
        return "\n".join([str(product) for product in self.__products])
