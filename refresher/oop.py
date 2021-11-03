class ClassTest:
    def instace_method(self):
        '''
         used for most things: produce an action 
         with the data inside an object, or if you
         want to modify the data inside an object
        '''
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        '''
         commonly used as factories
        '''
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        '''
         used to place a method inside a class
        '''
        print("Called static_method.")


############ factory example
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, type, weight):
        self.name = name
        self.type = type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.type}, wighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)


a_book = Book.hardcover("Harry Potter", 1500)
another_book = Book.paperback("Harry Potter", 200)

print(a_book)
print(another_book)