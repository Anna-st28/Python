import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        print("***\n" * 3)

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self):
        print("*******\n" * 3)

    def info(self):
        print("===Квадрат===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw(self):
        print("     *\n    ***\n   *****\n  *******\n *********\n***********")

    def info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 2: {self.side3}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area():.2f}")
        print(f"Периметр: {self.perimeter():.1f}")
        self.draw()


square = Square(3, "red")
rectangle = Rectangle(3, 7, "green")
triangle = Triangle(11, 6, 6, "yellow")

shapes = [square, rectangle, triangle]

for shape in shapes:
    shape.info()
