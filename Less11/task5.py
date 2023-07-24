"""Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""


class Retangle:
    """Документация из домашки"""

    def __init__(self, wight: float, height=None):
        self.wight = wight
        if height is None:
            self.height = wight
        else:
            self.height = height

    def perimetr(self):
        return (self.height + self.wight) * 2

    def area(self):
        return (self.height * self.wight)

    def __add__(self, other):
        per = self.perimetr() + other.perimetr()
        wigth = self.wight + other.wight
        height = per / 2 - wigth
        return Retangle(wigth, height)

    def __sub__(self, other):
        if self.perimetr() < other.perimetr():
            self, other = other, self
        wigth = abs(self.wight - other.wight)
        per = self.perimetr() + other.perimetr()
        height = per / 2 - wigth
        return Retangle(wigth, height)

    #def __str__(self):
    #    return f"Периметр: {self.perimetr()}"

    def __repr__(self):
       return f"Периметр: {self.perimetr()}"

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()


if __name__ == "__main__":
    re1 = Retangle(1, 4)
    re2 = Retangle(25, 5)
    print(re1 - re2)
    print(re1 < re2)
    print(repr(re2+re1))
    print(Retangle.__doc__)
