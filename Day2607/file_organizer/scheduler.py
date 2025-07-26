import schedule
import time
from organizer import organize_by_extension

def schedule_organize(path, interval=1):
    schedule.every(interval).minutes.do(organize_by_extension, path=path)
    print(f"Scheduled file organization every {interval} minute(s). Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped scheduling.")
