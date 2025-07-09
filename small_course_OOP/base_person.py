class Person:
    """Создаём человека"""

    def __init__(self, name, age, height):
        """Инициализация атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = f"Имя его {self.name}, возраст {self.age}, рост {self.height} см, вес {self.weight} пельменей"
        print(description)

    def get_weight(self):
        """Получение веса человека"""
        print(f"Вес нашего человека: {self.weight} кг")

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс воин"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса водителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print(f"Заряд ярости равен {self.rage} чубак")

    def description_person(self):
        """Получение описания воина"""
        description = f"Имя воина {self.name}, возраст {self.age}, заряд ярости {self.rage} чубак"
        print(description)

    def update_rage(self, power):
        """Обновление заряда ярости"""
        self.rage = power

