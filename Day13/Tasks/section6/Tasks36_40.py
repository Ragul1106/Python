# Task 36: Override __add__() in a Vector class to allow vector addition using +.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Task 37: Override __len__() in a Playlist class to return number of songs.
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

# Task 38: Override __getitem__() and __setitem__() in a class that mimics a shopping cart.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, item, quantity):
        self.items[item] = quantity

# Task 39: Override __contains__() in a custom Inventory class to check if item exists.
class Inventory:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

# Task 40: Create a class Money and implement __eq__, __gt__, __lt__ for comparing amounts.
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount