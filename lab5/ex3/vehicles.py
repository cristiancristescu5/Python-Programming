class Vehicle:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def compute_mileage(self):
        pass

    def compute_towing_cap(self):
        pass

    def __str__(self):
        return f"Vehicle mark: {self.mark}, vehicle model: {self.model}, year:{self.year}"


class Car(Vehicle):
    def __init__(self, mark, model, year, vtype='car', towing_capacity=1000):
        super().__init__(mark, model, year)
        self.vtype = vtype
        self.towing_capacity = towing_capacity

    def compute_towing_cap(self):
        return self.towing_capacity

    def compute_mileage(self):
        return (2023 - self.year) * 10_000


class Motorcycle(Vehicle):
    def __init__(self, mark, model, year, vtype='motorcycle', towing_capacity=100):
        super().__init__(mark, model, year)
        self.vtype = vtype
        self.towing_capacity = towing_capacity

    def compute_towing_cap(self):
        return self.towing_capacity

    def compute_mileage(self):
        return (2023 - self.year) * 8000


class Truck(Vehicle):
    def __init__(self, mark, model, year, vtype='truck', towing_capacity=1000):
        super().__init__(mark, model, year)
        self.vtype = vtype
        self.towing_capacity = towing_capacity

    def compute_mileage(self):
        return (2023 - self.year) * 15000

    def compute_towing_cap(self):
        return 24 * 1000
