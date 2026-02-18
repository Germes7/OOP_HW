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

# Метод звуков издаваемые животным
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

# Задача №2
# **Ключевые сущности** (класс)
# - Член общества: сущность (см. класс)
# - Возраст: float
# - Артефакт: str
# - Дата: int
# - Одежда: str

# **Дата** (класс)
# -День: int
# -Месяц: int

# **Член общества** (класс)
#  *Методы класса (self):
# - Волшебник: трах-тибедох_тит
# - Ведьма: варит зелье
# - Колдун: колдует, взмахивая посохом
# - Алхимик: наивный, пытается добыть философский камень

# **Взаимодействие сущностей** (метод)
# - Волшебник: муж ведьмы
# - Ведьма: жена волшебника
# - Колдун: любовник ведьмы (на то она и ведьма)
# - Алхимик: старый девственник. "Мальчик для битья" для ведьмы с колдуном

# Класс Член общества
class Society_member:

    wizard: str
    witch: str
    witcher: str
    alchemist: str

    def __init__(self, wizard: str, witch: str, witcher: str, alchemist: str):

        self.wizard = wizard
        self.witch = witch
        self.witcher = witcher
        self.alchemist = alchemist

    def action(self):

        if self.wizard:
            return f"{self.wizard} трах-тибедох_тит"

        elif self.witch:
            return f"{self.witch} варит зелье"

        elif self.witcher:
            return f"{self.witcher} колдует"

        else:
            return f"{self.alchemist} наивный, пытается добыть философский камень"