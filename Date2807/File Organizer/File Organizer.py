import os
import shutil
from functools import wraps
from typing import Dict, Generator, Tuple

DEFAULT_CATEGORIES: Dict[str, str] = {

    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'webp': 'Images',
    'svg': 'Images',
    'bmp': 'Images',
    'tiff': 'Images',

    'pdf': 'Documents',
    'doc': 'Documents',
    'docx': 'Documents',
    'xls': 'Documents',
    'xlsx': 'Documents',
    'ppt': 'Documents',
    'pptx': 'Documents',
    'txt': 'Documents',
    'rtf': 'Documents',
    'odt': 'Documents',
 
    'zip': 'Archives',
    'rar': 'Archives',
    '7z': 'Archives',
    'tar': 'Archives',
    'gz': 'Archives',

    'mp3': 'Audio',
    'wav': 'Audio',
    'ogg': 'Audio',
    'flac': 'Audio',
    'aac': 'Audio',

    'mp4': 'Videos',
    'mov': 'Videos',
    'avi': 'Videos',
    'mkv': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',

    'py': 'Code',
    'js': 'Code',
    'html': 'Code',
    'css': 'Code',
    'cpp': 'Code',
    'java': 'Code',
    'php': 'Code',
    'json': 'Code',
    'xml': 'Code',

    'exe': 'Executables',
    'msi': 'Executables',
    'dmg': 'Executables'
}

class FileOrganizer:
    def __init__(self, categories: Dict[str, str] = None):
        self.categories = categories or DEFAULT_CATEGORIES
        self.other_folder = "Other"
    
    def dry_run(func):
        """Decorator to preview changes without actually moving files"""
        @wraps(func)
        def wrapper(self, directory: str, *args, **kwargs):
            print(f"\nDRY RUN: Previewing changes for '{directory}'")
            print("=" * 50)

            moved_files = list(self._files_to_organize(directory))
            total_files = len(moved_files)
            
            if not moved_files:
                print("No files to organize found.")
                return

            for source, destination in moved_files:
                print(f"Would move: {os.path.basename(source)} -> {destination}")
            
            print("\nSummary:")
            print(f"Total files to organize: {total_files}")
            print("No files were actually moved (dry run mode)")
            print("=" * 50)

            return func(self, directory, *args, **kwargs)
        return wrapper
    
    def _get_file_category(self, extension: str) -> str:
        """Determine the category folder for a file extension"""
        return self.categories.get(extension.lower(), self.other_folder)
    
    def _files_to_organize(self, directory: str) -> Generator[Tuple[str, str], None, None]:
        """Generator: Yield (source_path, destination_folder) for each file"""
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            if os.path.isdir(filepath):
                continue

            _, ext = os.path.splitext(filename)
            ext = ext[1:]  

            category = self._get_file_category(ext)
            dest_folder = os.path.join(directory, category)
            
            yield (filepath, dest_folder)
    
    def organize_files(self, directory: str) -> Generator[Tuple[str, str], None, None]:
        """Organize files in the directory by extension"""
        if not os.path.isdir(directory):
            raise ValueError(f"Directory does not exist: {directory}")
        
        moved_files = []
        
        for source, dest_folder in self._files_to_organize(directory):
            try:
              
                os.makedirs(dest_folder, exist_ok=True)

                dest_path = os.path.join(dest_folder, os.path.basename(source))
                shutil.move(source, dest_path)
                
                moved_files.append((source, dest_path))
                yield (source, dest_path)
                
            except PermissionError as e:
                print(f"Permission denied: {e}")
            except Exception as e:
                print(f"Error moving {source}: {e}")
        
        return moved_files
    
    @dry_run
    def preview_organization(self, directory: str):
        """Preview what organize_files would do (uses dry_run decorator)"""
        return self._files_to_organize(directory)

def main():
    print("File Organizer")
    print("==============")
    print("This tool organizes files into folders by their extensions.\n")

    while True:
        directory = input("Enter directory path to organize (or 'quit' to exit): ").strip()
        
        if directory.lower() in ['quit', 'exit']:
            print("Goodbye!")
            return
        
        if not os.path.isdir(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            continue
        
        break
    
    organizer = FileOrganizer()
    
    while True:
        print("\nOptions:")
        print("1. Preview organization (dry run)")
        print("2. Organize files")
        print("3. Change directory")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            organizer.preview_organization(directory)
        elif choice == "2":
            print(f"\nOrganizing files in '{directory}'...")
            moved_count = 0
            
            for source, dest in organizer.organize_files(directory):
                print(f"Moved: {os.path.basename(source)} -> {os.path.dirname(dest)}")
                moved_count += 1
            
            print(f"\nDone! Organized {moved_count} files.")
        elif choice == "3":
            new_dir = input("Enter new directory path: ").strip()
            if os.path.isdir(new_dir):
                directory = new_dir
                print(f"Directory changed to '{directory}'")
            else:
                print(f"Error: Directory '{new_dir}' does not exist.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()