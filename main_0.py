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

    def __str__(self):
        return f"{self.day} дня, {self.month} месяца"

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

    def __str__(self):
        return f"Волшебный предмет: {self.accessory}. Сделан из {self.material} имеет силу {self.power}. Используется: {self.artifact_action()}"


# Класс сущности
# Статус в обществе, одежда, стаж, артефакт
class IndividualMagic:
    society: str
    cloth: str
    experience: int
    artifact: Artifact
    data: Data

    def __init__(self, society: str, cloth: str, experience: int, artifact: Artifact, data: Data):

        self.society = society
        self.cloth = cloth
        self.experience = experience
        self.artifact = artifact
        self.data = data

    def action(self):

        if self.society.lower() == "волшебник":
            return f"{self.society} трах-тибедох_тит. Муж ведьмы"

        elif self.society.lower() == "ведьма":
            return f"{self.society} варит зелье. Жена волшебника"

        elif self.society.lower() == "колдун":
            return f"{self.society} колдует. Любовник ведьмы"

        elif self.society.lower() == "алхимик":
            return f"{self.society} наивный, пытается добыть философский камень. Мальчик для битья -для всех остальных"

        else:
            return f"{self.society} кто-то пришлый. Может даже волхв!"

    def __str__(self):
        return f"Член общества: {self.society} одет в {self.cloth}. Опыт {self.experience}, владеет {self.artifact}. Происходит сие безобразие {self.data}. Отношение в своем обществе {self.action()}"


# Задача №3
# **Ключевые сущности**
# - Фермер: строка
# - Покупатель: строка
# - Товар: строка
# - Рынок, объеденяющий в себе вышеперечисленные классы

# **Структура сущности**
# - Фермер: Человек -продает товар
# - Покупатель: Человек -покупает товар
# - Товар: простая жратва

# **Влияние характеристик сущностей на взаимодействие промеж себя**
# - Фермер: продает товар и коммуницирует с Покупателем, в тайне желая его обвесить
# - Покупатель: покупает товар у продавца. Страстно желая скинуть цену на покупаемый товар
# - Товар: опять-таки, просто жратва. Переходящая от Продавца к Покупателю.

# Клас Витрина (перечень)
class Showcase:

    view: str

    def __init__(self, view: str):

        self.view = view

    

class Product:


class Farmer:
    pass

class Buyer:
    pass


