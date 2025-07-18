from book_manager.book_ops import add_book, list_books, list_genres
from user_manager.user_ops import borrow_book, return_book

books = {}
borrowed_books = {}

def main():
    while True:
        print("\n1. Add Book\n2. List Books\n3. List Genres\n4. Borrow Book\n5. Return Book\n6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            book_id = (isbn,)
            add_book(books, book_id, title, author, genre)

        elif choice == "2":
            list_books(books)

        elif choice == "3":
            list_genres(books)

        elif choice == "4":
            user = input("Enter your name: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            book_id = (isbn,)
            borrow_book(books, borrowed_books, book_id, user)

        elif choice == "5":
            user = input("Enter your name: ")
            isbn = input("Enter ISBN of the book to return: ")
            book_id = (isbn,)
            return_book(books, borrowed_books, book_id, user)

        elif choice == "6":
            break

        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
