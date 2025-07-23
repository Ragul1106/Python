import os
from datetime import datetime

def get_file_metadata(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return []

    file_data = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            created = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
            modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
            file_data.append((filename, size, created, modified))
    return file_data

def export_to_txt(data, output_file="file_report.txt"):
    with open(output_file, "w") as f:
        f.write("Filename\tSize(Bytes)\tCreated\t\t\tModified\n")
        f.write("-" * 80 + "\n")
        for item in data:
            f.write(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\n")
    print(f"✅ Metadata report saved to {output_file}")

def main():
    print("📁 File Metadata Viewer")
    folder = input("Enter the folder path: ").strip()
    data = get_file_metadata(folder)
    if data:
        print(f"\nFound {len(data)} files.\n")
        export_to_txt(data)

if __name__ == "__main__":
    main()
