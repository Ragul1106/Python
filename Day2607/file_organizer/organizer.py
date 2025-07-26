import os
import shutil

def organize_by_extension(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1][1:].lower() or "others"
            folder = os.path.join(path, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(full_path, os.path.join(folder, file))
    print("Files organized by extension.")
