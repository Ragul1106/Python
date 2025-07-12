playlist = ['Song 1', 'Song 2']

def add_song():
    song = input("Song to add: ")
    playlist.append(song)
    print(f"Added {song}")

def repeat_playlist():
    times = int(input("Repeat how many times? "))
    print(f"\nRepeated Playlist: {playlist * times}")

def search_song():
    song = input("Search song: ")
    print(f"{song} {'found' if song in playlist else 'not found'}")
add_song()
repeat_playlist()
search_song()