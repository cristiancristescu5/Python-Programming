class Account:
    def __init__(self, amount, cap, accountNumber):
        self.money = amount
        self.maxCapacity = cap
        self.accountNumber = accountNumber

    def withdraw(self, amount):
        if amount > self.money:
            print("You don't have enough money")
        else:
            self.money -= amount
            print(f"Withdrew ${amount}. New balance: ${self.money}")
            return amount

    def deposit(self, amount):
        if self.money + amount > self.maxCapacity:
            print(f"Overflow: max capacity = {self.maxCapacity}")
        else:
            print(f"Old sold: {self.money}")
            self.money += amount
            print(f"Your new sold: {self.money}")

    def __str__(self):
        return f"Bank account: {self.accountNumber}, balance = {self.money}, max capacity = {self.maxCapacity}"

    def calculate_interest(self, period=1):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, amount=0, cap=10_000, interest_rate=0.02):
        super().__init__(amount, cap, account_number)
        self.interest_rate = interest_rate

    def calculate_interest(self, period=1):
        interest = self.money * self.interest_rate * period
        self.money += interest
        print(f"The interest for {period} years is: {interest}. Your new balance is: {self.money}")


class CheckingAccount(Account):
    def __init__(self, account_number, amount=0, cap=10_000, interest_rate=0.4):
        super().__init__(amount, cap, account_number)
        self.interest_rate = interest_rate

    def calculate_interest(self, period=1):
        interest = self.money * self.interest_rate * period
        self.money += interest
        print(f"The interest for {period} years is: {interest}. Your new balance is: {self.money}")
