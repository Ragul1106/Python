import os
from datetime import datetime

def backup_file():
    source = input("Enter source file path: ")

    if not os.path.isfile(source):
        print("❌ File not found!")
        return

    filename, ext = os.path.splitext(os.path.basename(source))
    backup_name = f"{filename}_backup{ext}"
    backup_path = os.path.join(os.path.dirname(source), backup_name)

    if os.path.exists(backup_path):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_name = f"{filename}_backup_{timestamp}{ext}"
        backup_path = os.path.join(os.path.dirname(source), backup_name)

    try:
        with open(source, 'r') as src, open(backup_path, 'w') as dest:
            content = src.read()
            dest.write(content)
        print(f"✅ Backup created: {backup_path}")
    except Exception as e:
        print(f"⚠️ Error while backing up: {e}")

if __name__ == "__main__":
    backup_file()
