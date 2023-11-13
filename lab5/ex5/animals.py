class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.warmBlood = True

    def give_birth(self):
        print(f"{self.name} gives birth to live young ones.")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.can_fly = True

    def fly_and_lay_egs(self):
        print(f"{self.name} can fly and lays eggs")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_gills = True

    def swim(self):
        print(f"{self.name} can swim.")
