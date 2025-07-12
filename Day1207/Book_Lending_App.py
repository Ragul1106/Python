books = ["Book1", "Book2", "Book3"]
borrowed = []

def borrow_book():
    print("\nAvailable Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
    
    try:
        choice = int(input("Select book to borrow: ")) - 1
        book = books.pop(choice)
        borrowed.append(book)
        print(f"You borrowed: {book}")
    except (ValueError, IndexError):
        print("Invalid selection")

def return_book():
    if not borrowed:
        print("No books borrowed")
        return
    
    print("\nBorrowed Books:")
    for i, book in enumerate(borrowed, 1):
        print(f"{i}. {book}")
    
    try:
        choice = int(input("Select book to return: ")) - 1
        book = borrowed.pop(choice)
        books.append(book)
        print(f"You returned: {book}")
    except (ValueError, IndexError):
        print("Invalid selection")

while True:
    print("\n1. Borrow Book\n2. Return Book\n3. Show Available\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        borrow_book()
    elif choice == '2':
        return_book()
    elif choice == '3':
        print("\nAvailable Books:", books)
    elif choice == '4':
        break
    else:
        print("Invalid choice")