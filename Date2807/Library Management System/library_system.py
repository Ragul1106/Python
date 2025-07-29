import json
from datetime import datetime, timedelta
from functools import wraps

# Decorator: Admin-only access
def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        password = input("Enter admin password: ")
        if password == "admin123":
            return func(*args, **kwargs)
        else:
            print("❌ Unauthorized access.")
    return wrapper

# Book class
class Book:
    def __init__(self, title, author, available=True, borrower=None, due_date=None):
        self.title = title
        self.author = author
        self.available = available
        self.borrower = borrower
        self.due_date = due_date

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available,
            "borrower": self.borrower,
            "due_date": self.due_date
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"], data["author"],
            data["available"], data["borrower"], data["due_date"]
        )

    def __str__(self):
        return f"📖 Title: {self.title} | Author: {self.author} | Available: {self.available} | Due: {self.due_date}"

# Library class
class Library:
    def __init__(self, filepath="library_data.json"):
        self.books = {}
        self.filepath = filepath
        self.load_data()

    def save_data(self):
        with open(self.filepath, "w") as f:
            json.dump({title: book.to_dict() for title, book in self.books.items()}, f)

    def load_data(self):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.books = {title: Book.from_dict(b) for title, b in data.items()}
        except FileNotFoundError:
            self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print("⚠️ Book already exists.")
        else:
            self.books[title] = Book(title, author)
            self.save_data()
            print("✅ Book added.")

    def borrow_book(self, title, borrower):
        try:
            book = self.books[title]
            if book.available:
                book.available = False
                book.borrower = borrower
                book.due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                self.save_data()
                print("📚 Book borrowed.")
            else:
                print("❌ Book is already borrowed.")
        except KeyError:
            print("❌ Book not found.")

    def return_book(self, title):
        try:
            book = self.books[title]
            if not book.available:
                book.available = True
                book.borrower = None
                book.due_date = None
                self.save_data()
                print("✅ Book returned.")
            else:
                print("⚠️ Book was not borrowed.")
        except KeyError:
            print("❌ Book not found.")

    def search_book(self, title):
        try:
            print(self.books[title])
        except KeyError:
            print("❌ Book not found.")

    def list_overdue_books(self):
        today = datetime.now().date()
        print("📆 Overdue Books:")
        found = False
        for book in self.books.values():
            if not book.available and book.due_date:
                due = datetime.strptime(book.due_date, "%Y-%m-%d").date()
                if due < today:
                    print(book)
                    found = True
        if not found:
            print("✅ No overdue books.")

    @admin_only
    def delete_book(self, title):
        if title in self.books:
            del self.books[title]
            self.save_data()
            print("🗑️ Book deleted.")
        else:
            print("❌ Book not found.")

    def __iter__(self):
        return (book for book in self.books.values() if book.available)

# CLI Menu
if __name__ == "__main__":
    library = Library()

    while True:
        print("\n📚 LIBRARY MENU")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. List Overdue Books")
        print("6. List Available Books")
        print("7. Delete Book (Admin)")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            title = input("Enter book title: ")
            borrower = input("Enter your name: ")
            library.borrow_book(title, borrower)

        elif choice == "3":
            title = input("Enter book title: ")
            library.return_book(title)

        elif choice == "4":
            title = input("Enter book title: ")
            library.search_book(title)

        elif choice == "5":
            library.list_overdue_books()

        elif choice == "6":
            print("✅ Available Books:")
            for book in library:
                print(book)

        elif choice == "7":
            title = input("Enter book title to delete: ")
            library.delete_book(title)

        elif choice == "8":
            print("👋 Exiting Library System.")
            break

        else:
            print("❌ Invalid choice.")
