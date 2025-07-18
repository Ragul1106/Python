from weather_data.fetch_weather import fetch_weather

def main():
    while True:
        print("\n====== City Weather Report ======")
        print("1. Check Weather")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            city = input("Enter city name: ").strip()
            fetch_weather(city)
        elif choice == "2":
            print("Exiting Weather Report...")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
