class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"You have checked out '{title}' by {book.author}.")
                    return
                else:
                    print(f"'{title}' by {book.author} is currently checked out.")
                    return
        print(f"'{title}' is not available in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"You have returned '{title}' by {book.author}.")
                    return
                else:
                    print(f"'{title}' by {book.author} is already available in the library.")
                    return
        print(f"'{title}' is not available in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"  {book.title} by {book.author}")
        else:
            print("No books are currently available.")