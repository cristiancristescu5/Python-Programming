class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if self.items.count(item) != 0:
            print("Item already exists")
        else:
            self.items.append(item)

    def check_out(self, item):
        if self.items.count(item) == 0:
            print("Item does not exist")
        else:
            self.items.remove(item)
            item.is_checked_out = True
            return item.get_price(), item

    def return_item(self, item):
        if self.items.count(item) != 0:
            print("Item already exists")
        else:
            item.is_checked_out = False
            self.items.append(item)
            return item.get_price

    def list_items(self):
        for i in self.items:
            i.display_info()


class LibraryItem:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.is_checked_out = False
        self.price = price

    def get_price(self):
        return self.price

    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre

    def display_info(self):
        print(f"Book title: {self.title}, Author: {self.author}, Genre: {self.genre}, Price: {self.price}")


class DVD(LibraryItem):
    def __init__(self, title, author, price, duration):
        super().__init__(title, author, price)
        self.duration = duration

    def display_info(self):
        print(f"DVD Title: {self.title}, Author: {self.author}, Duration:{self.duration} minutes, Price: {self.price}")


class Magazine(LibraryItem):
    def __init__(self, title, author, price, dom):
        super().__init__(title, author, price)
        self.dom = dom

    def display_info(self):
        print(f"Magazine: {self.title}, Author: {self.author}, Subject: {self.dom}, Price: {self.price}")
