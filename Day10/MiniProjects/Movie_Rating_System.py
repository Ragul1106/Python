movies = {}

def add_movie(name, genre):
    movies[name] = {"ratings": [], "genre": genre}

def add_rating(name, rating):
    movies[name]["ratings"].append(rating)
    movies[name]["avg_rating"] = sum(movies[name]["ratings"])/len(movies[name]["ratings"])

def top_movies():
    return sorted(movies.items(), 
                 key=lambda x: x[1]["avg_rating"], 
                 reverse=True)
    
add_movie("Inception", "Sci-Fi")
add_rating("Inception", 5)
print("Top movies:", top_movies())