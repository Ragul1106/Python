movies = (
    input("Enter first favorite movie: "),
    input("Enter second favorite movie: "),
    input("Enter third favorite movie: ")
)

print("\nAll movies:", movies)
print("\nIndividual movies:")
for i, movie in enumerate(movies, 1):
    print(f"Movie {i}: {movie}")

print(f"\nType of movies variable: {type(movies)}")