### custom errors
class CantReadMorePagesThanBookLength(ValueError):
    pass

### class
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return (
            f"<Book {self.name}, read {self.pages_read} of {self.page_count} pages."
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise CantReadMorePagesThanBookLength(
                f"You tried reading more pages than the book has"
            )
        self.pages_read += pages
        print(f"Pages read: {self.pages_read}")

### driver code
a_book = Book("This is a title", 50)
a_book.read(49)
a_book.read(51)