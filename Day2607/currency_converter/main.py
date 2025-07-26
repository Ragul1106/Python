from converter import convert_amount, get_rate
from favorites import load_favorites, save_favorite, show_favorites
from plotter import plot_trend

def main():
    while True:
        print("\n💱 Currency Converter")
        print("1. Convert Currency")
        print("2. Lookup Historical Rate")
        print("3. Show Favorite Currencies")
        print("4. Add to Favorites")
        print("5. Show Exchange Trend")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            from_cur = input("From Currency (e.g. USD): ").upper()
            to_cur = input("To Currency (e.g. INR): ").upper()
            amount = float(input("Amount: "))
            result, rate = convert_amount(amount, from_cur, to_cur)
            if result:
                print(f"{amount} {from_cur} = {result:.2f} {to_cur} (Rate: {rate:.4f})")
            else:
                print("Conversion failed.")

        elif choice == "2":
            from_cur = input("From Currency: ").upper()
            to_cur = input("To Currency: ").upper()
            date = input("Date (YYYY-MM-DD): ")
            rate = get_rate(from_cur, to_cur, date)
            if rate:
                print(f"Rate on {date}: 1 {from_cur} = {rate} {to_cur}")
            else:
                print("Could not fetch historical rate.")

        elif choice == "3":
            show_favorites()

        elif choice == "4":
            currency = input("Enter currency code to add: ").upper()
            save_favorite(currency)

        elif choice == "5":
            from_cur = input("From Currency: ").upper()
            to_cur = input("To Currency: ").upper()
            plot_trend(from_cur, to_cur)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
