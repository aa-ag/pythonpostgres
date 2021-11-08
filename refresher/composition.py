class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"


###### DRIVER CODE ######
a_book = ("Intro to Python")
another_book = ("Intermediate Python")
yet_another_book = ("Advanced Python")

a_bookself = Bookshelf(a_book, another_book, yet_another_book)
print(a_bookself)