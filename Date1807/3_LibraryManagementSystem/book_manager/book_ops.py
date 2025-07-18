def add_book(book_db, book_id, title, author, genre):
    if book_id in book_db:
        print("Book already exists.")
    else:
        book_db[book_id] = {
            "title": title,
            "author": author,
            "genre": genre,
            "available": True
        }
        print(f"Book '{title}' added.")

def list_books(book_db):
    if not book_db:
        print("No books available.")
        return
    print("\nLibrary Books:")
    for book_id, info in book_db.items():
        status = "Available" if info["available"] else "Borrowed"
        print(f"ISBN: {book_id[0]}, Title: {info['title']}, Author: {info['author']}, Genre: {info['genre']}, Status: {status}")

def list_genres(book_db):
    genres = set(book["genre"] for book in book_db.values())
    if genres:
        print("Available Genres:", ", ".join(genres))
    else:
        print("No genres available.")
