import os

def find_largest_files(path, top_n=5):
    files = []
    for root, _, filenames in os.walk(path):
        for f in filenames:
            full_path = os.path.join(root, f)
            size = os.path.getsize(full_path)
            files.append((full_path, size))
    files.sort(key=lambda x: x[1], reverse=True)
    print(f"\nTop {top_n} Largest Files:")
    for f, s in files[:top_n]:
        print(f"{f} — {s/1024:.2f} KB")
