# TODO: : Learn about subclasses in python

import math


class Shape:
    def __init__(self, color: int, is_boundary: bool) -> None:
        self.color: int = color
        self.is_boundary: bool = is_boundary

    def describe(self):
        print(f" It is {self.color} ")


class Circle(Shape):
    def __init__(self, radius: int, color: int, is_boundary: bool) -> None:
        super().__init__(color, is_boundary)
        self.radius: int = radius

    def area_of_circle(self):
        super().describe()
        return math.pi * self.radius * 2


class Square(Shape):
    def __init__(self, color: int, is_boundary: bool, width: int) -> None:
        super().__init__(color, is_boundary)
        self.width: int = width


circle = Circle(radius=5, color=23, is_boundary=True)
print(circle.color)
print(circle.radius)
print(circle.is_boundary)
print(circle.area_of_circle())
