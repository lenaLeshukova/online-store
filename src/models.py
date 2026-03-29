from typing import Any, cast


class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    def __add__(self, other: Any) -> float:
        """Сложение только объектов одного класса"""
        if type(self) is not type(other):
            raise TypeError("Можно складывать товары только одного класса")
        result = cast(float, (self.price * self.quantity) + (
                other.price * other.quantity))
        return result

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
                return  # Завершаем метод, не меняя цену

        self.__price = new_price


class Smartphone(Product):
    """Подкласс Смартфон"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int,
                 efficiency: float, model: str, memory: int,
                 color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Подкласс Трава газонная"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int,
                 country: str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
        """Метод добавляет продукт в список. Проверка через isinstance
        перед добавлением"""

        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, возвращает строковое представление списка товаров"""
        product_strings = []
        for product in self.__products:
            # шаблон "Название, цена руб. Остаток: кол-во шт."
            product_strings.append(
                f"{product.name}, "
                f"{product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_strings)
