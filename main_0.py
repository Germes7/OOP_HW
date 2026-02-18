# Задание №3

# Задача №1
# **Характеристики животных**
#
# - Имя: строка
# - Вид: строка (например, собака, кошка, попугай, удав)
# - Возраст: целое число (в годах)
# - Вес: вещественное число (в килограммах)
# - Вакцинирован: булево значение (да/нет)


# Класс хозяин
class Owner:

    name: str

    def __init__(self, name: str):

        self.name = name

# Класс животное
class Pet:

    name: str
    view: str
    age: int
    weight: float
    is_vaccine: bool
    lord: Owner

    def __init__(self, name: str, view: str, age: int, weight: float, is_vaccine: bool, lord: Owner):

        self.name = name
        self.view = view
        self.age = age
        self.weight = weight
        self.is_vaccine = is_vaccine
        self.lord = lord

        if age <= 0:
            raise ValueError("Возраст питомца, не может быть меньше или равным нулю")

        if weight <= 0:
            raise ValueError("Вес не может быть меньшим либо равным нулю")

    def action(self):

        if self.view.lower() == "удав":
            return f"{self.view} шипит"

        elif self.view.lower() == "пес":
            return f"{self.view} лает"

        elif self.view.lower() == "кот":
            return f"{self.view} мяукает"

        elif self.view.lower() == "попугай":
            return f"{self.view} кричит Полундра!"

        else:
            return f"{self.view} что-то орет"

