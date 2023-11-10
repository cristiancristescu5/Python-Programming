from ex1.shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def compute_perimeter(self):
        return 2 * pi * self.r

    def compute_area(self):
        return pi * self.r * self.r

    def __str__(self):
        return str(f"radius = {self.r}")
