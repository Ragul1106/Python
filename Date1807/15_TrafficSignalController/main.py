from traffic_control.controller import update_signal, display_signals

signals = {
    ("Main Street", "08:00"): "Green",
    ("Main Street", "08:30"): "Red",
    ("2nd Ave", "08:00"): "Yellow"
}

active_signals = set([("Main Street", "08:00"), ("2nd Ave", "08:00")])

def main():
    while True:
        print("\n1. View Signals\n2. Update Signal\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_signals(signals, active_signals)

        elif choice == "2":
            location = input("Enter location: ")
            time = input("Enter time (HH:MM): ")
            status = input("Enter status (Green/Yellow/Red): ")
            signal_id = (location.strip(), time.strip())
            update_signal(signals, active_signals, signal_id, status)

        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
