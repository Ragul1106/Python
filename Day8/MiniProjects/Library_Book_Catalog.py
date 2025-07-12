books = [['Python Basics', 'John Doe'], ['Clean Code', 'Robert Martin']]

def add_book():
    title = input("Book title: ")
    author = input("Author: ")
    books.append([title, author])

def search_book():
    title = input("Search book: ")
    for book in books:
        if title.lower() in book[0].lower():
            print(f"Found: {book[0]} by {book[1]}")
            return
    print("Book not found")

def show_recent():
    print("\nRecent Additions:")
    for book in books[-3:]:
        print(f"{book[0]} by {book[1]}")

add_book()
search_book()
show_recent()