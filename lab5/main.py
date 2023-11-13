from ex1.circle import Circle
from ex1.rectangle import Rectangle
from ex1.triangle import Triangle
from ex2.account import Account, SavingsAccount, CheckingAccount
from ex3.vehicles import Motorcycle, Car, Truck
import ex6.library as lib

print("-----------------------------ex1--------------------------------\n")
x = Circle(4)
y = Rectangle(5, 5)
z = Triangle(3, 4, 5)
print(x)
print(y)
print(z)
print("--------------------------ex2---------------------------------\n")

sacc = SavingsAccount(account_number=123, cap=10_000, amount=10)
sacc.deposit(1000)
sacc.deposit(10_000)
sacc.withdraw(100)
sacc.calculate_interest()

cacc = CheckingAccount(134, 100, 10_000)
cacc.deposit(100)
cacc.deposit(800)
cacc.withdraw(10)
cacc.calculate_interest()

print(cacc)
print(sacc)

print("-----------------------------ex6--------------------------------------\n")

item1 = lib.Book("Ion", "Liviu Rebreanu", 10, "Drama")
item2 = lib.DVD("BAu", "Cineva", 100, 100)

library = lib.Library()
library.add_item(item2)
library.add_item(item1)

p, item = library.check_out(item1)

item.display_info()
print("_______________________________________________")
library.list_items()
print("________________________________________________")
library.return_item(item)

library.list_items()

