import os

def bulk_rename(path, prefix="file", start=1):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for idx, name in enumerate(files, start=start):
        ext = os.path.splitext(name)[1]
        new_name = f"{prefix}_{idx}{ext}"
        os.rename(os.path.join(path, name), os.path.join(path, new_name))
    print("Files renamed successfully.")
