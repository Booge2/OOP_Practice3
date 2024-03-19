class User:
    """
    Реалізує клас «Користувач» з атрибутами «ім'я», «вік» та «email».
    """

    def __init__(self, name: str, age: int, email: str):
        """
        Ініціалізація екземпляра класу «Користувач».

        Аргументи:
            name: Ім'я користувача.
            age: Вік користувача.
            email: Email-адреса користувача.
        """
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self) -> str:
        """
        Повертає ім'я користувача.
        """
        return self.__name

    def set_name(self, new_name: str):
        """
        Змінює ім'я користувача.

        Аргументи:
            new_name: Нове ім'я користувача.
        """
        self.__name = new_name

    def get_age(self) -> int:
        """
        Повертає вік користувача.
        """
        return self.__age

    def get_email(self) -> str:
        """
        Повертає email-адресу користувача.
        """
        return self.__email

    def __str__(self):
        """
        Повертає рядок з інформацією про користувача.
        """
        return f"""
        **Ім'я:** {self.get_name()}
        **Вік:** {self.get_age()}
        **Email:** {self.get_email()}
        """


user1 = User(
    name="Іван",
    age=25,
    email="ivan@example.com",
)

print(user1)

print(user1.get_name())
user1.set_name("Петро")
print(user1.get_name())

print(user1.get_age())
print(user1.get_email())


# Завдання 2
class ShoppingCart:
    """
    Реалізує клас «Кошик для покупок» з можливістю додавання товарів та підрахунку загальної вартості.
    """

    def __init__(self):
        """
        Ініціалізація екземпляра класу «Кошик для покупок».
        """
        self.__items = {}

    def add_item(self, item_name: str, price: float, quantity: int):
        """
        Додає товар до кошика.

        Аргументи:
            item_name: Назва товару.
            price: Ціна товару.
            quantity: Кількість товару.
        """
        if item_name in self.__items:
            self.__items[item_name]["quantity"] += quantity
        else:
            self.__items[item_name] = {"price": price, "quantity": quantity}

    def remove_item(self, item_name: str):
        """
        Видаляє товар з кошика.

        Аргументи:
            item_name: Назва товару.
        """
        if item_name in self.__items:
            del self.__items[item_name]

    def get_total_price(self) -> float:
        """
        Повертає загальну вартість товарів у кошику.

        Повертає: Загальна вартість товарів.
        """
        total_price = 0
        for item_name, item_info in self.__items.items():
            total_price += item_info["price"] * item_info["quantity"]
        return total_price

    def decrease_item_quantity(self, item_name: str, quantity: int):
        """
        Зменшує кількість одиниць товару в кошику.

        Аргументи:
            item_name: Назва товару.
            quantity: Кількість одиниць, на яку потрібно зменшити.
        """
        if item_name in self.__items:
            if quantity <= 0:
                raise ValueError("Не можна зменшити кількість на негативне значення")
            if self.__items[item_name]["quantity"] < quantity:
                raise ValueError("Недостатня кількість товару")
            self.__items[item_name]["quantity"] -= quantity

    def __str__(self):
        """
        Повертає рядок з інформацією про товари в кошику.
        """
        items_str = "\n".join(
            f"- {item_name}: {item_info['quantity']} шт. ({item_info['price']} грн/шт.)"
            for item_name, item_info in self.__items.items()
        )
        return f"""
        **Кошик для покупок:**

        {items_str}

        **Загальна вартість:** {self.get_total_price()} грн.
        """


cart = ShoppingCart()

cart.add_item("Яблуко", 5, 2)
cart.add_item("Банан", 7, 3)
cart.add_item("Молоко", 25, 1)

print(cart)

cart.decrease_item_quantity("Яблуко", 1)
cart.remove_item("Банан")

try:
    cart.decrease_item_quantity("Яблуко", 2)
except ValueError as e:
    print(e)
print(cart)

print(f"Загальна вартість: {cart.get_total_price()} грн.")


# Завдання 3
class EWallet:
    """
    Реалізує клас «Електронний Гаманець» з можливістю додавання, видалення та перевірки балансу.
    """

    def __init__(self, balance: float = 0.0):
        """
        Ініціалізація екземпляра класу «Електронний Гаманець».

        Аргументи:
            balance: Початковий баланс гаманця (опціонально).
        """
        self.__balance = balance

    def add_money(self, amount: float):
        """
        Додає кошти на гаманець.

        Аргументи:
            amount: Сума, яку потрібно додати.
        """
        if amount < 0:
            raise ValueError("Не можна додати негативну суму")
        self.__balance += amount

    def remove_money(self, amount: float):
        """
        Видаляє кошти з гаманця.

        Аргументи:
            amount: Сума, яку потрібно видалити.
        """
        if amount < 0:
            raise ValueError("Не можна видалити негативну суму")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        self.__balance -= amount

    def get_balance(self) -> float:
        """
        Повертає баланс гаманця.

        Повертає:
            Баланс гаманця.
        """
        return self.__balance

    def __str__(self):
        """
        Повертає рядок з інформацією про баланс гаманця.
        """
        return f"**Баланс:** {self.get_balance()} грн."


wallet = EWallet()

wallet.add_money(100)
print(wallet)

wallet.remove_money(50)
print(wallet)

try:
    wallet.remove_money(100)
except ValueError as e:
    print(e)

print(wallet.get_balance())


# Завдання 4
class Computer:
    """
    Реалізує клас «Комп'ютер» з інформацією про процесор, ОЗУ та відеокарту.
    """

    def __init__(self, cpu: str, ram: int, gpu: str):
        """
        Ініціалізація екземпляра класу «Комп'ютер».

        Аргументи:
            cpu: Модель процесора.
            ram: Обсяг оперативної пам'яті.
            gpu: Модель відеокарти.
        """
        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu

    def get_cpu(self) -> str:
        """
        Повертає модель процесора.

        Повертає: Модель процесора.
        """
        return self.__cpu

    def get_ram(self) -> int:
        """
        Повертає обсяг оперативної пам'яті.

        Повертає: Обсяг оперативної пам'яті.
        """
        return self.__ram

    def get_gpu(self) -> str:
        """
        Повертає модель відеокарти.

        Повертає: Модель відеокарти.
        """
        return self.__gpu

    def __str__(self):
        """
        Повертає рядок з інформацією про комп'ютер.
        """
        return f"""
        **Процесор:** {self.get_cpu()}
        **ОЗУ:** {self.get_ram()} ГБ
        **Відеокарта:** {self.get_gpu()}
        """


computer = Computer(
    cpu="AMD Ryzen 5 5600H",
    ram=16,
    gpu="NVIDIA GeForce RTX 3050",
)

print(computer)

print(computer.get_cpu())
print(computer.get_ram())
print(computer.get_gpu())
