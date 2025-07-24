class InvalidCategoryError(Exception):
    pass

def expense_tracker():
    expenses = {}
    total = 0.0
    
    while True:
        try:
            category = input("Enter category (or 'done' to finish): ").lower()
            if category == 'done':
                break
                
            if category not in ['food', 'transport', 'entertainment', 'utilities']:
                raise InvalidCategoryError("Invalid category")
                
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            expenses[category] = expenses.get(category, 0) + amount
            total += amount
            
        except InvalidCategoryError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print(f"Current total: ${total:.2f}")
    
    print("\nExpense Summary:")
    for category, amount in expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")
    print(f"Total: ${total:.2f}")

expense_tracker()