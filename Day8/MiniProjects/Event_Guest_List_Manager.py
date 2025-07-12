guests = ['Alice', 'Bob']

def add_guest():
    name = input("Guest name: ")
    if name in guests:
        print("Already invited!")
    else:
        guests.append(name)
        print(f"Added {name}")

def check_guest():
    name = input("Check guest: ")
    print(f"{name} is {'invited' if name in guests else 'not invited'}")

def show_guests():
    print(f"\nGuest List ({len(guests)}):")
    for guest in guests:
        print(f"- {guest}")

add_guest()
check_guest()
show_guests()