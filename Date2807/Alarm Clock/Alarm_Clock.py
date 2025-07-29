import time
from datetime import datetime
from playsound import playsound
from functools import wraps

def snooze(delay_seconds=300): 
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            choice = input("Snooze for 5 minutes? (y/n): ").strip().lower()
            if choice == 'y':
                print(f"Snoozing for {delay_seconds // 60} minutes...")
                time.sleep(delay_seconds)
                func(*args, **kwargs)
        return wrapper
    return decorator

@snooze(delay_seconds=300)
def set_alarm(alarm_time):
    try:
        print(f"Alarm set for {alarm_time}")
        while True:
            now = datetime.now().strftime("%H:%M")
            if now == alarm_time:
                print("Wake up! Alarm ringing...")
                playsound("alarm.mp3")  
                break
            time.sleep(1)
    except ValueError:
        print("Invalid time format. Please use HH:MM (24-hour format).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_time = input("Enter alarm time (HH:MM): ")
    set_alarm(user_time)
