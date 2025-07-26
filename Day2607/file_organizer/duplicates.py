import os
import hashlib

def file_hash(file_path):
    hash_algo = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def remove_duplicates(path):
    hashes = {}
    duplicates = []
    for root, _, files in os.walk(path):
        for name in files:
            full_path = os.path.join(root, name)
            h = file_hash(full_path)
            if h in hashes:
                duplicates.append(full_path)
                os.remove(full_path)
            else:
                hashes[h] = full_path
    print(f"{len(duplicates)} duplicate file(s) removed.")
