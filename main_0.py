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

# Класс Дата
class Data:

    day: int
    month: int

    def __init__(self, day: int, month: int):

        self.day = day
        self.month = month

        if not day > 0 and not day < 32:
            return ValueError("Дней в месяце должно быть больше нуля и меньше 31") #февраль и високосные года не рассматриваем (пока)

        if not month > 0 and not month < 13:
            return  ValueError("Месяцев от 1 до 12")

# Класс Артефакт
# название артефакта, материал, сила
class Artifact:

    accessory: str
    material: str
    power: str

    def __init__(self, accessory: str, material: str, power: int):

        self.accessory = accessory
        self.material = material
        self.power = power

    def artifact_action(self):

        if self.accessory.lower() == "волшебная палочка":
            return f"{self.accessory} машет как умалишенный"

        elif self.accessory.lower() == "котелок":
            return f"{self.accessory} ставит на костер"

        elif self.accessory.lower() == "посох":
            return f"{self.accessory} может и по хребтине навернуть"

        elif self.accessory.lower() == "реторта":
            return f"{self.accessory} греется на Бунзеновской горелке"

        else:
            return f"{self.accessory} -официальная наука, умывает руки. Что с этим делать?!"


# Класс сущности
class Individual_magic:
    society: str
    witch: str
    witcher: str
    alchemist: str

    def __init__(self, society: str, artefact: str, witcher: str, alchemist: str):

        self.society = society
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

