books = [['Python Basics', 50, 200], ['Clean Code', 100, 300]]

def update_progress():
    title = input("Book title: ")
    for book in books:
        if book[0] == title:
            pages = int(input("Pages read: "))
            book[1] += pages
            if book[1] >= book[2]:
                print(f"Finished {title}!")
            return
    print("Book not found")

def show_progress():
    print("\nReading Progress:")
    for book in books:
        print(f"{book[0]}: {book[1]}/{book[2]} pages")

update_progress()
show_progress()