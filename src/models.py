from abc import ABC, abstractmethod
from typing import Any, cast


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float,
                 quantity: int):
        # Сохраняем базовые атрибуты здесь
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


class LogMixin:
    """Миксин для логирования создания объекта"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        # Печатаем инфо о создании ДО передачи аргументов дальше
        print(
            f"Создан объект: {self.__class__.__name__}"
            f"({', '.join([repr(a) for a in args])})"
        )
        # используется repr(a), чтобы строковые значения выводились в кавычках
        # (как в задании: 'Продукт1').
        # Передаем ВСЕ аргументы следующему классу в цепочке (BaseProduct)
        super().__init__(*args, **kwargs)


class Product(LogMixin, BaseProduct):
    """Класс для представления товара, наследует миксин и абстрактный класс"""

    # Миксин идет первым, чтобы при вызове super().__init__ сначала
    # сработал конструктор миксина
    # Добавляем эту строку, чтобы mypy "увидел" скрытый атрибут родителя
    _BaseProduct__price: float

    def __init__(self, name: str, description: str, price: float,
                 quantity: int) -> None:

        #  Вызываем super() и передаем аргументы в LogMixin
        super().__init__(name, description, price, quantity)

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
        # Доступ к приватному атрибуту родителя
        return self._BaseProduct__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с валидацией и подтверждением снижения"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self._BaseProduct__price:
            user_answer = input(
                f"Вы уверены, что хотите снизить цену с"
                f" {self._BaseProduct__price} "
                f"до {new_price}? (y/n): ")
            if user_answer.lower() != 'y':
                print("Действие отменено.")
                return  # Завершаем метод, не меняя цену

        self._BaseProduct__price = new_price


class Smartphone(Product):
    """Подкласс Смартфон"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int,
                 efficiency: float, model: str, memory: int,
                 color: str) -> None:
        # Передаем аргументы в Product, который передаст в миксин через super
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
