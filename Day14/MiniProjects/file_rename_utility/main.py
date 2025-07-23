import os

def rename_txt_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    if not files:
        print("📭 No .txt files found.")
        return

    for idx, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)
        new_filename = f"file_{idx}.txt"
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path):
            print(f"⚠️ {new_filename} already exists. Skipping.")
            continue

        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_filename}")

if __name__ == "__main__":
    folder = input("Enter folder path containing .txt files: ").strip()
    rename_txt_files(folder)
