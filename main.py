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
