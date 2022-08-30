import math
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a **2

class Circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return math.pi * self.r **2
# Создаем прямоугольники и выводим их площадь
rect_1 = Rectangle(5,4)
rect_2 = Rectangle(10, 15)

# Создаем квадраты и выводим их площадь
sqd_1 = Square(7)
sqd_2 = Square(8)

# Создаем круги и выводим их площадь
cirl_1 = Circle(10)
cirl_2 = Circle(100)

figures = [rect_1, rect_2, sqd_1, sqd_2, cirl_1, cirl_2]
for figure in figures:
    if isinstance(figure, Square):
        print("Площадь квардата - ", figure.get_area_square())
    elif isinstance(figure, Circle):
        print("Площадь круга - ", round(figure.get_area_circle()))
    else:
        print("Площадь прямоугольника - ", figure.get_area())


