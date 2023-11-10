from ex1.shape import Shape


class Rectangle(Shape):
    def __init__(self, l, L):
        self.l = l
        self.L = L

    def compute_area(self):
        return self.l * self.L

    def compute_perimeter(self):
        return 2 * (self.l + self.L)

    def __str__(self):
        return f"rectangle: l = {self.l}, L = {self.L}"