class Person:
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print('Запущен __init__')

    def sing(self):
        """Просим человека спеть"""
        print(self.name + ' поёт')

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + ' танцует')

man = Person('Андрей', 31)
woman = Person('Танюха', 29)
# print(man.name)  Андрей
# print(woman.age) 29
man.dance() # Андрей танцует
woman.sing() # Танюха поёт
