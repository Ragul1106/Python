FAV_FILE = "favorites.txt"

def load_favorites():
    try:
        with open(FAV_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return []

def save_favorite(currency):
    favs = load_favorites()
    if currency not in favs:
        favs.append(currency)
        with open(FAV_FILE, "w") as f:
            for c in favs:
                f.write(c + "\n")
        print(f"{currency} added to favorites.")

def show_favorites():
    favs = load_favorites()
    print("★ Favorite Currencies:")
    for c in favs:
        print(f"- {c}")
