# Задание №3

# Задача №1
# **Характеристики животных**
#
# - Имя: строка
# - Вид: строка (например, собака, кошка, попугай)
# - Возраст: целое число (в годах)
# - Вес: вещественное число (в килограммах)
# - Вакцинирован: булево значение (да/нет)

class Pet:

    name: str
    view: str
    age: int
    weight: float
    is_vaccine: bool

    def __init__(self, name: str, view: str, age: int, weight: float, is_vaccine: bool):

        self.name = name
        self.view = view
        self.age = age
        self.weight = weight
        self.is_vaccine = is_vaccine

        if age <= 0:
            raise ValueError("Возраст питомца, не может быть меньше или равным нулю")
