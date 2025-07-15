books = {}

def add_book(book_id, title, author, copies):
    books[book_id] = {"title": title, "author": author, "copies": copies}

def borrow_book(book_id):
    if books.get(book_id, {}).get("copies", 0) > 0:
        books[book_id]["copies"] -= 1

def return_book(book_id):
    books[book_id]["copies"] += 1

def available_books():
    return {bid: data for bid, data in books.items() 
            if data["copies"] > 0}

add_book(1, "Python Basics", "Heera", 5)
borrow_book(1)
print("Available:", available_books())