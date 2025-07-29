import os
import zipfile
import schedule
import time
from datetime import datetime

def scheduled(interval="daily"):
    def decorator(func):
        if interval == "daily":
            schedule.every().day.at("00:00").do(func)
        elif interval == "hourly":
            schedule.every().hour.do(func)
        elif interval == "minute":
            schedule.every(1).minutes.do(func)
        return func
    return decorator

class Backup:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        os.makedirs(self.backup_dir, exist_ok=True)

    def _get_file_list(self):
        for root, _, files in os.walk(self.source_dir):
            for file in files:
                yield os.path.join(root, file)

    def _backup_name(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.backup_dir, f"backup_{timestamp}.zip")

    def create_backup(self):
        try:
            backup_path = self._backup_name()
            with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for filepath in self._get_file_list():
                    arcname = os.path.relpath(filepath, self.source_dir)
                    zipf.write(filepath, arcname)
                    print(f"✅ Added: {arcname}")
            print(f"\n🎉 Backup completed successfully: {backup_path}")
        except FileNotFoundError as e:
            print(f"[❌ Error] File not found: {e}")
        except Exception as e:
            print(f"[❌ Error] {e}")


@scheduled("minute")  
def run_backup():
    backup = Backup("my_files", "my_backups")
    backup.create_backup()


if __name__ == "__main__":
    print("🛡️ Automated Backup Script Running...\n")
    while True:
        schedule.run_pending()
        time.sleep(1)
