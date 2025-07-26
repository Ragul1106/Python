from generator import generate_multiple
from strength import calculate_strength
from saver import save_passwords, read_passwords

def get_bool_input(prompt):
    return input(prompt + " (y/n): ").lower() == 'y'

def main():
    while True:
        print("\n🔐 Password Generator")
        print("1. Generate Passwords")
        print("2. View Saved Passwords")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            count = int(input("How many passwords to generate? "))

            use_upper = get_bool_input("Include uppercase letters?")
            use_lower = get_bool_input("Include lowercase letters?")
            use_digits = get_bool_input("Include numbers?")
            use_symbols = get_bool_input("Include symbols?")

            passwords = generate_multiple(
                count,
                length=length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_digits=use_digits,
                use_symbols=use_symbols
            )

            print("\nGenerated Passwords:")
            for p in passwords:
                print(f"{p}  --> Strength: {calculate_strength(p)}")

            save = get_bool_input("\nDo you want to save these passwords?")
            if save:
                save_passwords(passwords)

        elif choice == "2":
            saved = read_passwords()
            if not saved:
                print("No saved passwords.")
            else:
                print("\n🔐 Saved Passwords:")
                for idx, pw in enumerate(saved, 1):
                    print(f"{idx}. {pw}")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
