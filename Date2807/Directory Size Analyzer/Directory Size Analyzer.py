import os
from pathlib import Path
from functools import wraps

def human_readable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        size = func(*args, **kwargs)
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
    return wrapper

class DirectoryAnalyzer:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.sizes = {}

    def analyze(self):
        for foldername, subfolders, filenames in os.walk(self.root_dir):
            try:
                total = 0
                for f in filenames:
                    try:
                        path = Path(foldername) / f
                        size = path.stat().st_size
                        total += size
                    except Exception as e:
                        print(f"Error accessing file {f}: {e}")
                self.sizes[foldername] = total
            except Exception as e:
                print(f"Permission error on folder {foldername}: {e}")

    def get_directory_sizes(self):
        return self.sizes

    def get_large_files(self, threshold):
        for foldername, subfolders, filenames in os.walk(self.root_dir):
            for f in filenames:
                try:
                    path = Path(foldername) / f
                    size = path.stat().st_size
                    if size >= threshold:
                        yield path, size
                except Exception as e:
                    continue

    @human_readable
    def total_size(self):
        return sum(self.sizes.values())

if __name__ == "__main__":
    path = input("Enter directory path to analyze: ")
    analyzer = DirectoryAnalyzer(path)
    analyzer.analyze()

    print("\nDirectory Sizes:")
    for dir_path, size in analyzer.get_directory_sizes().items():
        print(f"{dir_path}: {human_readable(lambda: size)()}")

    print("\nLarge Files (>10MB):")
    for file_path, size in analyzer.get_large_files(10 * 1024 * 1024):
        print(f"{file_path}: {human_readable(lambda: size)()}")

    print(f"\nTotal Size: {analyzer.total_size()}")
