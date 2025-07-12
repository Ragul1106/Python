watchlist = ['Inception', 'The Shawshank Redemption']

def add_movie():
    movie = input("Enter movie to add: ")
    watchlist.append(movie)
    print(f"Added {movie}")

def watched_movie():
    movie = input("Enter watched movie: ")
    if movie in watchlist:
        watchlist.remove(movie)
        print(f"Marked {movie} as watched")
    else:
        print("Movie not in watchlist")

def show_watchlist():
    print("\nYour Watchlist:")
    for i, movie in enumerate(watchlist[:5], 1):
        print(f"{i}. {movie}")

add_movie()
watched_movie()
show_watchlist()