def borrow_book(book_db, borrow_db, book_id, user):
    if book_id not in book_db:
        print("Book not found.")
        return
    if not book_db[book_id]["available"]:
        print("Book is already borrowed.")
        return

    book_db[book_id]["available"] = False
    borrow_db[book_id] = user
    print(f"{user} borrowed the book '{book_db[book_id]['title']}'.")

def return_book(book_db, borrow_db, book_id, user):
    if book_id not in borrow_db:
        print("This book was not borrowed.")
        return
    if borrow_db[book_id] != user:
        print("You did not borrow this book.")
        return

    book_db[book_id]["available"] = True
    del borrow_db[book_id]
    print(f"{user} returned the book '{book_db[book_id]['title']}'.")
