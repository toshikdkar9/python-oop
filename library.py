class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        raise NotImplementedError("Subclasses must implement borrow().")

    def return_book(self):
        raise NotImplementedError("Subclasses must implement return_book().")

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    

class PhysicalBook(Book):
    def __init__(self, title, author, isbn, copies):
        super().__init__(title, author, isbn)
        self.copies = copies
        self.available = copies > 0

    def borrow(self):
        if self.copies == 0:
            raise Exception("No copies available.")

        self.copies -= 1

        if self.copies == 0:
            self.available = False

        print(f"Borrowed '{self.title}'.")

    def return_book(self):
        self.copies += 1
        self.available = True

        print(f"Returned '{self.title}'.")


class EBook(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)

    def borrow(self):
        print(f"Downloading '{self.title}'.")

    def return_book(self):
        print(f"'{self.title}' is an eBook. No return needed.")

from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    @abstractmethod
    def borrow(self): pass

    @abstractmethod
    def return_book(self): pass

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    MAX_BORROW_LIMIT = 3  # class variable — belongs to all members

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []  # single source of truth

    def borrow_book(self, book):
        if len(self.__borrowed_books) >= Member.MAX_BORROW_LIMIT:
            raise Exception("Borrowing limit reached.")
        book.borrow()
        self.__borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.__borrowed_books:
            raise Exception("This member didn't borrow this book.")
        book.return_book()
        self.__borrowed_books.remove(book)

    def get_borrow_count(self):
        return len(self.__borrowed_books)

    def get_borrowed_books(self):
        return list(self.__borrowed_books)  # return a copy, not the list itself

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            raise Exception("Member not registered.")

        if isbn not in self.books:
            raise Exception("Book not found.")

        member = self.members[member_id]
        book = self.books[isbn]

        member.borrow_book(book)

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            raise Exception("Member not registered.")

        if isbn not in self.books:
            raise Exception("Book not found.")

        member = self.members[member_id]
        book = self.books[isbn]

        member.return_book(book)

    def available_books(self):
        return [book for book in self.books.values() if book.available]

    def member_summary(self, member_id):
        if member_id not in self.members:
            raise Exception("Member not found.")

        member = self.members[member_id]

        print(f"\nMember: {member.name}")
        print("Borrowed Books:")

        if not member.borrowed_books:
            print("None")
        else:
            for book in member.borrowed_books:
                print(book)