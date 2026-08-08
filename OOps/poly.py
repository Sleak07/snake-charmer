# To learn about Polymorphism

from abc import ABC, abstractmethod
from typing import override


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    @override
    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side: float = side

    @override
    def area(self):
        return self.side**2


class Biscuit(Square):
    def __init__(self, side: float, wing: str) -> None:
        super().__init__(side)
        self.wing: str = wing


shapes = [Circle(3.8), Square(1.9), Biscuit(2.7, "Bat")]

for shape in shapes:
    print(shape.area())
