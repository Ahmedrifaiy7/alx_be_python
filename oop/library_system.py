# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        """Initialize book attributes: title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of a basic book."""
        return f"Book: {self.title} by {self.author}"

# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes, including those from the base class."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes, including those from the base class."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class demonstrating composition
class Library:
    def __init__(self):
        """Initialize the Library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
