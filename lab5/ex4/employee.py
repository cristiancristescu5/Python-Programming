class Employee:
    def __init__(self, salary, name):
        self.name = name
        self.salary = salary

    def work(self):
        pass

    def __str__(self):
        return f"Employee: {self.name}, has salary = {self.salary}\n"


class Manager(Employee):
    def __init__(self, salary, name, department):
        super().__init__(salary, name)
        self.department = department

    def work(self):
        print(f"Manager: {self.name} has the salary = {self.salary} and si managing the department: {self.department}")


class Engineer(Employee):
    def __init__(self, salary, name, specialty):
        super().__init__(salary, name)
        self.specialty = specialty

    def work(self):
        print(f"Engineer: {self.name} has the salary = {self.salary} and is specialized in {self.specialty}")


class SalesPerson(Employee):
    def __init__(self, salary, name, region):
        super().__init__(salary, name)
        self.region = region

    def work(self):
        print(f"Salesperson: {self.name} has the salary = {self.salary} and sells products in the region {self.region}")
