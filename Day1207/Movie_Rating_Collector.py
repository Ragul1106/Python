movies = []

def add_movie():
    name = input("Enter movie name: ")
    rating = float(input("Enter your rating (1-5): "))
    movies.append({"name": name, "rating": rating})
    print("Rating added!")

def show_top_movies():
    if not movies:
        print("No movies rated yet")
        return
    
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    print("\nTop Rated Movies:")
    for i, m in enumerate(sorted_movies[:3], 1):
        print(f"{i}. {m['name']} - {m['rating']}/5")

while True:
    print("\n1. Add Movie Rating\n2. Show Top Movies\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_movie()
    elif choice == '2':
        show_top_movies()
    elif choice == '3':
        break
    else:
        print("Invalid choice")