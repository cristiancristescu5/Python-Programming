from ex1.shape import Shape
import math


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compute_perimeter(self):
        return self.a + self.b + self.c

    def compute_area(self):
        semi = self.compute_perimeter() / 2
        return math.sqrt(semi * (semi - self.a) * (semi - self.b) * (semi - self.c))
