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
        description = f"Имя: {self.name}, возраст: {self.age}, рост: {self.height} см, вес: {self.weight} кг"
        print(description)

    def get_weight(self):
        """Получение веса человека"""
        print(f"Вес нашего человека: {self.weight} кг")

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

print('***Class Person ***')
man = Person('Андрей', 31, 173)
man.description_person() # Имя: Андрей, возраст: 31, рост: 173, вес: 60
man.wight = 110
man.get_weight()
man.update_weight(110) # Меняем на 110 кг
man.get_weight() # вызываем метод Вес нашего человека 110 кг

print('\n***Class Warrior ***')
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

warrior = Warrior('Конор', 32, 200)
# warrior.update_weight(150) # Меняем вес Конора с 200 на 150
# warrior.description_person() # Имя: Конор, возраст: 32, рост: 200 см, вес: 110 кг

warrior.get_rage()
warrior.description_person()
warrior.update_rage(66)
warrior.get_rage()
warrior.description_person()