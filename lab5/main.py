from ex1.circle import Circle
from ex1.rectangle import Rectangle
from ex2.account import Account, SavingsAccount, CheckingAccount
from ex3.vehicles import Motorcycle, Car, Truck

sacc = SavingsAccount(account_number=123, cap=10_000, amount=10)
sacc.deposit(1000)
sacc.deposit(10_000)
sacc.withdraw(100)
sacc.calculate_interest()

x = Circle(4)
y = Rectangle(5, 5)
print(sacc)
print(x)
print(y)
