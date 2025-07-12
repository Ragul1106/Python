from datetime import datetime, timedelta

def calculate_due_date():
    book = input("Enter book name: ")
    borrow_date = input("Enter borrow date (DD-MM-YYYY): ")
    
    try:
        borrow_date = datetime.strptime(borrow_date, "%d-%m-%Y")
        due_date = borrow_date + timedelta(days=7)
        print(f"\nBook: {book}")
        print(f"Borrow Date: {borrow_date.strftime('%d-%m-%Y')}")
        print(f"Due Date: {due_date.strftime('%d-%m-%Y')}")
    except ValueError:
        print("Invalid date format. Use DD-MM-YYYY")

calculate_due_date()