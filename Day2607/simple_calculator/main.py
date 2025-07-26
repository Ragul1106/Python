import memory
import history
import unit_converter

def evaluate_expression(expr):
    try:
        result = eval(expr)
        history.add_history(expr, result)
        return result
    except Exception as e:
        return f"Error: {e}"

def memory_menu():
    print("\nMemory Menu:")
    print("1. Store current result")
    print("2. Recall memory")
    print("3. Clear memory")
    choice = input("Choose: ")
    if choice == "1":
        val = float(input("Enter value to store in memory: "))
        memory.store(val)
        print("Stored.")
    elif choice == "2":
        val = memory.recall()
        print(f"Memory: {val}")
    elif choice == "3":
        memory.clear()
        print("Memory cleared.")

def conversion_menu():
    print("\nUnit Conversion:")
    print("1. Length")
    print("2. Weight")
    c = input("Choose: ")

    value = float(input("Enter value to convert: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    if c == "1":
        try:
            converted = unit_converter.convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {converted:.2f} {to_unit}")
        except:
            print("Invalid length units.")
    elif c == "2":
        try:
            converted = unit_converter.convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {converted:.2f} {to_unit}")
        except:
            print("Invalid weight units.")
    else:
        print("Invalid choice.")

def main():
    print("📱 Simple Calculator")

    while True:
        print("\nOptions:")
        print("1. Evaluate Expression")
        print("2. Memory Functions")
        print("3. Show History")
        print("4. Unit Conversion")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            expr = input("Enter expression (supports +, -, *, /, ( )): ")
            result = evaluate_expression(expr)
            print("Result:", result)
        elif choice == "2":
            memory_menu()
        elif choice == "3":
            history.show_history()
        elif choice == "4":
            conversion_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
