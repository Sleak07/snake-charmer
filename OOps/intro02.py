import math


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def area_of_circle(self):
        return math.pi * self.radius * self.radius

    def perimeter_of_circle(self):
        return math.pi * self.radius * 2


if __name__ == "__main__":
    cir = Circle(radius=2.5)
    area = cir.area_of_circle()
    perimeter = cir.perimeter_of_circle()

    print("area_of_circle", area)
    print("perimeter_of_circle", perimeter)
