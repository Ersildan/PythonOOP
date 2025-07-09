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

man = Person('Андрей', 31, 173)

#man.description_person() # Имя: Андрей, возраст: 31, рост: 173, вес: 60
#man.wight = 110
#man.get_weight()
man.update_weight(110) # Меняем на 110 кг
man.get_weight() # вызываем метод Вес нашего человека 110 кг
