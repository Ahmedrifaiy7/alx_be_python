class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

class Library:
    def __init__(self):
        self.__books=[]

    def add_book(self, book):
        self.__books.append(book)

