# TODO: : Learn about subclasses in python

import math


class Shape:
    def __init__(self, area: float) -> None:
        self.area: float = area


class Circle(Shape):
    # Circle inherits from Shape
    def __init__(self, radius: float) -> None:
        self.radius: float = radius
        area: float = self.calculate_area()
        super().__init__(area)

    def calculate_area(self):
        return math.pi * self.radius**2


if __name__ == "__main__":
    cro = Circle(5.7)
    print(cro.calculate_area())
