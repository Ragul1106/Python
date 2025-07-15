distances = {}

def add_distance(city1, city2, distance):
    distances.setdefault(city1, {})[city2] = distance
    distances.setdefault(city2, {})[city1] = distance

def get_distance(city1, city2):
    return distances.get(city1, {}).get(city2, "Unknown")

add_distance("Chennai", "Bangalore", 350)
print("Distance:", get_distance("Chennai", "Bangalore"))