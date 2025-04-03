class Auto:
    def __init__(self, name="Неизвестно", year=2000, performance="Неизвестно",
                 power=150, color="Неизвестно", price=1000000):
        self.name = name
        self.year = year
        self.performance = performance
        self.power = power
        self.color = color
        self.price = price

    def input(self):
        self.name = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.performance = input("Введите производителя: ")
        self.power = int(input("Введите мощность двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = int(input("Введите цену: "))

    def output(self):
        print("********** Данные автомобиля **********")
        print(f"Название модели: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.performance}")
        print(f"Мощность двигателя: {self.power} л.с.")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
        print("========================================")

    def print_name(self):
        return self.name

    def set_price(self, new_price):
        self.price = new_price


my_auto = Auto("X7 M50i", 2021, "BMW", 530, "white", 10790000)
my_auto.output()

