from datetime import datetime
from typing import List, Dict, Any

class Product:
    """Базовый класс для всех товаров"""
    
    def __init__(self, product_id: int, name: str, price: float, quantity: int, manufacturer: str):
        self._id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity
        self._manufacturer = manufacturer
    
    # Геттеры
    def get_id(self) -> int:
        return self._id
    
    def get_name(self) -> str:
        return self._name
    
    def get_price(self) -> float:
        return self._price
    
    def get_quantity(self) -> int:
        return self._quantity
    
    def get_manufacturer(self) -> str:
        return self._manufacturer
    
    # Сеттеры
    def set_id(self, product_id: int):
        self._id = product_id
    
    def set_name(self, name: str):
        self._name = name
    
    def set_price(self, price: float):
        if price >= 0:
            self._price = price
        else:
            raise ValueError("Цена не может быть отрицательной")
    
    def set_quantity(self, quantity: int):
        if quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Количество не может быть отрицательным")
    
    def set_manufacturer(self, manufacturer: str):
        self._manufacturer = manufacturer
    
    # Методы
    def get_product_info(self) -> str:
        """Простой метод без параметров - возвращает информацию о товаре"""
        return f"Товар: {self._name}, Цена: {self._price} руб., В наличии: {self._quantity}"
    
    def apply_discount(self, discount_percent: float) -> float:
        """Метод с входными параметрами - применяет скидку"""
        if 0 <= discount_percent <= 100:
            discount = self._price * discount_percent / 100
            new_price = self._price - discount
            return new_price
        else:
            raise ValueError("Скидка должна быть в диапазоне 0-100%")
    
    def update_stock(self, change_amount: int, operation_type: str) -> Dict[str, Any]:
        """Метод с входными и выходными параметрами - обновляет складские запасы"""
        result = {"success": False, "message": "", "new_quantity": self._quantity}
        
        if operation_type == "add":
            self._quantity += change_amount
            result["success"] = True
            result["message"] = f"Товар добавлен. Новое количество: {self._quantity}"
            result["new_quantity"] = self._quantity
        elif operation_type == "remove":
            if change_amount <= self._quantity:
                self._quantity -= change_amount
                result["success"] = True
                result["message"] = f"Товар списан. Новое количество: {self._quantity}"
                result["new_quantity"] = self._quantity
            else:
                result["message"] = "Недостаточно товара на складе"
        else:
            result["message"] = "Неизвестная операция"
        
        return result
    
    def calculate_total_value(self) -> float:
        """Рассчитывает общую стоимость товара на складе"""
        return self._price * self._quantity


class WritingProduct(Product):
    """Класс для письменных принадлежностей (наследуется от Product)"""
    
    def __init__(self, product_id: int, name: str, price: float, quantity: int, 
                 manufacturer: str, color: str, ink_type: str):
        super().__init__(product_id, name, price, quantity, manufacturer)
        self._color = color
        self._ink_type = ink_type
    
    # Дополнительные геттеры
    def get_color(self) -> str:
        return self._color
    
    def get_ink_type(self) -> str:
        return self._ink_type
    
    # Дополнительные сеттеры
    def set_color(self, color: str):
        self._color = color
    
    def set_ink_type(self, ink_type: str):
        self._ink_type = ink_type
    
    # Переопределение метода (наследование)
    def get_product_info(self) -> str:
        """Переопределенный метод - возвращает расширенную информацию"""
        base_info = super().get_product_info()
        return f"{base_info}, Цвет: {self._color}, Тип чернил: {self._ink_type}"
    
    def check_ink_compatibility(self, paper_type: str) -> bool:
        """Проверяет совместимость чернил с типом бумаги"""
        compatible_combinations = {
            "gel": ["office", "glossy"],
            "ballpoint": ["office", "newspaper"],
            "fountain": ["writing", "office"]
        }
        return paper_type in compatible_combinations.get(self._ink_type, [])


class PaperProduct(Product):
    """Класс для бумажной продукции (наследуется от Product)"""
    
    def __init__(self, product_id: int, name: str, price: float, quantity: int,
                 manufacturer: str, paper_type: str, format: str):
        super().__init__(product_id, name, price, quantity, manufacturer)
        self._paper_type = paper_type
        self._format = format
    
    # Дополнительные геттеры
    def get_paper_type(self) -> str:
        return self._paper_type
    
    def get_format(self) -> str:
        return self._format
    
    # Дополнительные сеттеры
    def set_paper_type(self, paper_type: str):
        self._paper_type = paper_type
    
    def set_format(self, format: str):
        self._format = format
    
    # Переопределение метода
    def get_product_info(self) -> str:
        """Переопределенный метод - возвращает расширенную информацию"""
        base_info = super().get_product_info()
        return f"{base_info}, Тип бумаги: {self._paper_type}, Формат: {self._format}"
    
    def calculate_area(self) -> float:
        """Рассчитывает площадь листа бумаги"""
        format_sizes = {
            "A4": (0.21, 0.297),
            "A5": (0.148, 0.21),
            "A3": (0.297, 0.42)
        }
        if self._format in format_sizes:
            width, height = format_sizes[self._format]
            return width * height
        return 0.0


class Order:
    """Класс для управления заказами"""
    
    def __init__(self, order_id: int):
        self._order_id = order_id
        self._products = []
        self._total_amount = 0.0
        self._status = "created"
        self._order_date = datetime.now()
    
    # Геттеры
    def get_order_id(self) -> int:
        return self._order_id
    
    def get_products(self) -> List[Product]:
        return self._products
    
    def get_total_amount(self) -> float:
        return self._total_amount
    
    def get_status(self) -> str:
        return self._status
    
    def get_order_date(self) -> datetime:
        return self._order_date
    
    # Сеттеры
    def set_status(self, status: str):
        valid_statuses = ["created", "processing", "completed", "cancelled"]
        if status in valid_statuses:
            self._status = status
        else:
            raise ValueError(f"Статус должен быть одним из: {valid_statuses}")
    
    # Методы
    def add_product(self, product: Product, quantity: int = 1) -> bool:
        """Добавляет товар в заказ"""
        if product.get_quantity() >= quantity:
            # Создаем копию информации о товаре для заказа
            order_item = {
                'product': product,
                'quantity': quantity,
                'price': product.get_price()
            }
            self._products.append(order_item)
            self._total_amount += product.get_price() * quantity
            return True
        return False
    
    def remove_product(self, product_id: int) -> bool:
        """Удаляет товар из заказа"""
        for i, item in enumerate(self._products):
            if item['product'].get_id() == product_id:
                removed_item = self._products.pop(i)
                self._total_amount -= removed_item['price'] * removed_item['quantity']
                return True
        return False
    
    def calculate_discounted_total(self, discount_rules: Dict[str, float]) -> float:
        """Рассчитывает итоговую сумму со скидками"""
        total = self._total_amount
        discount = 0
        
        # Применяем правила скидок
        for rule, value in discount_rules.items():
            if rule == "bulk" and total > 1000:
                discount += total * value
            elif rule == "regular_customer":
                discount += total * value
        
        return total - discount
    
    def get_order_summary(self) -> Dict[str, Any]:
        """Возвращает сводку по заказу"""
        return {
            "order_id": self._order_id,
            "total_amount": self._total_amount,
            "discounted_total": self.calculate_discounted_total({"regular_customer": 0.1}),
            "product_count": len(self._products),
            "status": self._status,
            "order_date": self._order_date.strftime("%Y-%m-%d %H:%M:%S")
        }


# Демонстрация использования
if __name__ == "__main__":
    # Создаем товары
    pen = WritingProduct(1, "Ручка гелевая", 50.0, 100, "Pilot", "синий", "gel")
    notebook = PaperProduct(2, "Тетрадь", 120.0, 50, "Hatber", "офисная", "A5")
    
    # Демонстрация геттеров и сеттеров
    print("=== Демонстрация геттеров/сеттеров ===")
    print(f"Имя ручки: {pen.get_name()}")
    pen.set_price(45.0)
    print(f"Новая цена: {pen.get_price()}")
    
    # Демонстрация методов
    print("\n=== Демонстрация методов ===")
    print(pen.get_product_info())
    print(notebook.get_product_info())
    
    # Метод с входными параметрами
    new_price = pen.apply_discount(10)
    print(f"Цена со скидкой 10%: {new_price}")
    
    # Метод с входными и выходными параметрами
    stock_result = pen.update_stock(10, "remove")
    print(f"Обновление склада: {stock_result}")
    
    # Создаем заказ
    order = Order(1001)
    order.add_product(pen, 2)
    order.add_product(notebook, 1)
    
    print("\n=== Информация о заказе ===")
    summary = order.get_order_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Демонстрация наследования и полиморфизма
    print("\n=== Демонстрация полиморфизма ===")
    products = [pen, notebook]
    for product in products:
        print(product.get_product_info())
