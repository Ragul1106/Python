import json
import random
from functools import wraps
from typing import List, Dict, Generator, Optional

class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration 
    
    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration//60}:{self.duration%60:02d})"
    
    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'artist': self.artist,
            'duration': self.duration
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        return cls(data['title'], data['artist'], data['duration'])

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs: List[Song] = []
        self.current_index = 0
        self.repeat = False
    
    def add_song(self, song: Song) -> None:
        """Add a song to the playlist"""
        self.songs.append(song)
    
    def remove_song(self, index: int) -> None:
        """Remove a song by index"""
        if 0 <= index < len(self.songs):
            del self.songs[index]

            if self.current_index >= index and self.current_index > 0:
                self.current_index -= 1
    
    def shuffle(self) -> None:
        """Shuffle the playlist"""
        random.shuffle(self.songs)
        self.current_index = 0
    
    def next_song(self) -> Generator[Optional[Song], None, None]:
        """Generator: Yield next song in playlist"""
        while True:
            if not self.songs:
                yield None
            
            if self.current_index >= len(self.songs):
                if self.repeat:
                    self.current_index = 0
                else:
                    yield None
            
            yield self.songs[self.current_index]
            self.current_index += 1
    
    def save_to_file(self, filename: str) -> None:
        """Save playlist to JSON file"""
        data = {
            'name': self.name,
            'songs': [song.to_dict() for song in self.songs],
            'current_index': self.current_index,
            'repeat': self.repeat
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Playlist saved to {filename}")
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error saving playlist: {e}")
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Playlist':
        """Load playlist from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            playlist = cls(data['name'])
            playlist.songs = [Song.from_dict(song) for song in data['songs']]
            playlist.current_index = data.get('current_index', 0)
            playlist.repeat = data.get('repeat', False)
            
            return playlist
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            raise IOError(f"Error loading playlist: {e}")
    
    def __str__(self):
        return (f"Playlist: {self.name}\n"
                f"Total songs: {len(self.songs)}\n"
                f"Current position: {self.current_index + 1}/{len(self.songs)}")

def repeat(func):
    """Decorator to enable playlist repeating"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.repeat = True
        return func(self, *args, **kwargs)
    return wrapper

class MusicPlayer:
    def __init__(self):
        self.playlists: Dict[str, Playlist] = {}
        self.current_playlist: Optional[Playlist] = None
        self.song_generator: Optional[Generator] = None
    
    def create_playlist(self, name: str) -> Playlist:
        """Create a new playlist"""
        if name in self.playlists:
            print(f"Playlist '{name}' already exists")
            return self.playlists[name]
        
        playlist = Playlist(name)
        self.playlists[name] = playlist
        return playlist
    
    def load_playlist(self, filename: str) -> None:
        """Load a playlist from file"""
        try:
            playlist = Playlist.load_from_file(filename)
            self.playlists[playlist.name] = playlist
            print(f"Loaded playlist '{playlist.name}' from {filename}")
        except IOError as e:
            print(e)
    
    def save_playlist(self, playlist_name: str, filename: str) -> None:
        """Save a playlist to file"""
        if playlist_name not in self.playlists:
            print(f"Playlist '{playlist_name}' not found")
            return
        
        try:
            self.playlists[playlist_name].save_to_file(filename)
        except IOError as e:
            print(e)
    
    def play(self, playlist_name: str) -> None:
        """Start playing a playlist"""
        if playlist_name not in self.playlists:
            print(f"Playlist '{playlist_name}' not found")
            return
        
        self.current_playlist = self.playlists[playlist_name]
        self.song_generator = self.current_playlist.next_song()
        print(f"Now playing: {playlist_name}")
    
    def next(self) -> Optional[Song]:
        """Play next song in current playlist"""
        if not self.current_playlist or not self.song_generator:
            print("No playlist is currently playing")
            return None
        
        song = next(self.song_generator)
        if song:
            print(f"Now playing: {song}")
        else:
            print("Reached end of playlist")
        
        return song
    
    @repeat
    def repeat_playlist(self, playlist_name: str) -> None:
        """Enable repeat mode and play playlist"""
        self.play(playlist_name)

def main():
    player = MusicPlayer()

    sample_songs = [
        Song("Bohemian Rhapsody", "Queen", 354),
        Song("Imagine", "John Lennon", 183),
        Song("Hotel California", "Eagles", 390),
        Song("Sweet Child O'Mine", "Guns N' Roses", 356),
        Song("Smells Like Teen Spirit", "Nirvana", 301)
    ]
    
    print("Music Playlist Manager")
    print("======================")
    
    while True:
        print("\nMenu:")
        print("1. Create new playlist")
        print("2. Add songs to playlist")
        print("3. View playlists")
        print("4. Play playlist")
        print("5. Play next song")
        print("6. Shuffle playlist")
        print("7. Repeat playlist")
        print("8. Save playlist to file")
        print("9. Load playlist from file")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == "1":
            name = input("Enter playlist name: ")
            player.create_playlist(name)
            print(f"Created playlist '{name}'")
        
        elif choice == "2":
            playlist_name = input("Enter playlist name: ")
            if playlist_name not in player.playlists:
                print(f"Playlist '{playlist_name}' not found")
                continue
            
            print("\nAdd songs (leave blank to finish):")
            while True:
                title = input("Song title: ").strip()
                if not title:
                    break
                artist = input("Artist: ").strip()
                duration = input("Duration (seconds): ").strip()
                
                try:
                    duration = int(duration)
                    song = Song(title, artist, duration)
                    player.playlists[playlist_name].add_song(song)
                    print(f"Added '{title}' to '{playlist_name}'")
                except ValueError:
                    print("Invalid duration. Please enter a number.")
        
        elif choice == "3":
            if not player.playlists:
                print("No playlists available")
                continue
            
            print("\nYour Playlists:")
            for name, playlist in player.playlists.items():
                print(f"- {name}: {len(playlist.songs)} songs")
        
        elif choice == "4":
            playlist_name = input("Enter playlist name: ")
            player.play(playlist_name)
        
        elif choice == "5":
            player.next()
        
        elif choice == "6":
            if not player.current_playlist:
                print("No playlist is currently playing")
                continue
            
            player.current_playlist.shuffle()
            print("Playlist shuffled")
            player.song_generator = player.current_playlist.next_song()
        
        elif choice == "7":
            playlist_name = input("Enter playlist name: ")
            player.repeat_playlist(playlist_name)
        
        elif choice == "8":
            playlist_name = input("Enter playlist name: ")
            filename = input("Enter filename to save: ")
            player.save_playlist(playlist_name, filename)
        
        elif choice == "9":
            filename = input("Enter filename to load: ")
            player.load_playlist(filename)
        
        elif choice == "10":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()