bucket_list = ['Paris', 'Tokyo']

def add_place():
    place = input("Place to add: ")
    if place in bucket_list:
        print("Already in your list!")
    else:
        bucket_list.append(place)
        print(f"Added {place}")

def show_list():
    print("\nYour Travel Bucket List:")
    for place in bucket_list:
        print(f"- {place}")

add_place()
show_list()