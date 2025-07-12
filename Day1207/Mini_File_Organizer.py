files = ["file1.jpg", "file2.txt", "file3.jpg", "file4.py"]

def organize_files():
    categories = {}
    for file in files:
        ext = file.split('.')[-1]
        if ext not in categories:
            categories[ext] = []
        categories[ext].append(file)
    
    print("\nOrganized Files:")
    for ext, files in categories.items():
        print(f"{ext.upper()} files: {', '.join(files)}")

organize_files()