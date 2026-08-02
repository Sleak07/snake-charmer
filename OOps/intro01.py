# TODO :Circle Class for Area and Perimeter
#


PI = 3.14


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def area_circle(self):
        return PI * self.radius * self.radius

    def perimeter(self):
        return 2 * PI * self.radius


if __name__ == "__main__":
    cir = Circle(3.5)
    print("Area:", cir.area_circle())
    print("Perimeter:", cir.perimeter())
