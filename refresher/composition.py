class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books."


###### DRIVER CODE ######
shelf = Bookshelf(300)
print(shelf)