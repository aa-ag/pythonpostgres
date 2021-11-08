class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books."


class Book:
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name


###### DRIVER CODE ######
shelf = Bookshelf(300)
print(shelf)