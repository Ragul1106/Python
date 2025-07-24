class CircularPlaylist:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if not self.songs:
            raise StopIteration
        song = self.songs[self.index % len(self.songs)]
        self.index += 1
        return song

print("\nCircular Playlist:")
playlist = CircularPlaylist(["Song 1", "Song 2", "Song 3"])
for i, song in enumerate(playlist):
    print(song)
    if i >= 9:  
        break