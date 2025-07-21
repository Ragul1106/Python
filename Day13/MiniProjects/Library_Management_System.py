from datetime import datetime, timedelta

# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

# Abstract Person Class
class Person:
    def __init__(self, name):
        self.name = name

# Member Class
class Member(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__borrowed_books = []

    def borrow_book(self, book, due_date):
        if book.is_borrowed:
            print(f"{book.title} is already borrowed.")
        else:
            book.is_borrowed = True
            transaction = Transaction(book, self, due_date)
            self.__borrowed_books.append(transaction)
            print(f"{self.name} borrowed '{book.title}' until {due_date}.")

    def return_book(self, book):
        for t in self.__borrowed_books:
            if t.book == book:
                book.is_borrowed = False
                self.__borrowed_books.remove(t)
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} has not borrowed '{book.title}'.")

    def get_borrowed_books(self):
        return self.__borrowed_books

    def __str__(self):
        return f"Member: {self.name}, Books Borrowed: {len(self.__borrowed_books)}"

# Librarian Class
class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, library, isbn):
        for book in library.books:
            if book.isbn == isbn:
                library.books.remove(book)
                print(f"Book '{book.title}' removed from library.")
                return
        print("Book not found.")

# Transaction Class
class Transaction:
    def __init__(self, book, member, due_date):
        self.book = book
        self.member = member
        self.due_date = due_date

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.name}, due on {self.due_date}"

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to library.")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        print(f"Search results for '{keyword}':")
        for book in results:
            print(book)

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Library with {len(self.books)} books and {len(self.members)} members."

# # Setup
# library = Library()
# librarian = Librarian("Ranjith")
# member1 = Member("Rocky")

# # Add Books
# book1 = Book("Python Basics", "Ragul", "111")
# book2 = Book("Data Science 101", "Arul", "222")
# librarian.add_book(library, book1)
# librarian.add_book(library, book2)

# # Add Member
# library.add_member(member1)

# # Search Books
# library.search_books("Python")

# # Borrow Book
# member1.borrow_book(book1, datetime.now().date() + timedelta(days=14))

# # Return Book
# member1.return_book(book1)

# # Print Info
# print(member1)
# print(library)
# print(f"Total books in library: {len(library)}")
