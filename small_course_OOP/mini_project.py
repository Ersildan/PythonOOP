class Car:
    """Создаём класс машина"""

    def __init__(self, model, year, engine, price, miles):
        """Инициализируем атрибуты машины"""
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.miles = miles
        self.wheels = 4

    def description_car(self):
        """Описание машины"""
        description = (f'Эту малышку называют "{self.model}", так как она {self.year} года выпуска.\n'
                       f'{self.engine} литров объем двигателя, а отдать придётся {self.price} шаверм.\n'
                       f'Кстати, её пробег мал всего лишь {self.miles} миль. И у модели {self.wheels} колеса.')
        print(description)

car = Car('Москвич2000', 2000, 5, 3000000, 100)
car.description_car()

print("\n*****")
print(f'Часть запросов к экземпляру:', car.model, car.price, car.year)
print("*****\n")

class Truck(Car):
    """Создаём класс машина"""

    def __init__(self, model, year, engine, price, miles):
        """Инициализируем атрибуты класса Грузовика"""
        super().__init__(model, year, engine, price, miles)
        self.wheels = 8

    def description_truck(self):
        """Описание Камаза"""
        description = (f"{self.model} это то, что нам не стыдно показывать с {self.year} года.\n"
                      f"{self.wheels} ми колесный зверь для строительства дорог, конечно, есть {self.model + 'и'} и с 10 тью.\n"
                      f"Но что вы мне сделаете, это же фэнтези мир 😄. Камаз с {self.engine} л объемом двигателя.\n"
                      f"Пробег этого богатыря {self.miles} км, а цена: {self.price} $")
        return description

    def get_signal(self):
        print(f'{self.model} делает Бип БЫЫЫбииииБ!')

truck = Truck('Камазик',1990, 11.76, 157894.74, 119446.0)
print(truck.description_truck())

print("\n*****")
print(f'Сколько колёс у {truck.model + "а"}:', truck.wheels)
print("*****\n")

truck.get_signal() # Бонус