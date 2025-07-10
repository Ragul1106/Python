items = input("Enter items (comma separated): ").split(',')
formatted = ", ".join(items[:-1]) + f", and {items[-1]}" if len(items) > 1 else items[0]
print(f"You bought {formatted}.")