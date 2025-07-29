import time
import json
import pygame
from functools import wraps

# Initialize pygame for sound
pygame.mixer.init()

# ---------- Decorator ----------
def notify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("🔔 Pomodoro Session Completed!")
        try:
            pygame.mixer.music.load("alarm.mp3")  # Ensure this file exists
            pygame.mixer.music.play()
        except Exception as e:
            print("Failed to play sound:", e)
    return wrapper

# ---------- Generator ----------
def countdown_generator(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        yield f"{mins:02d}:{secs:02d}"
        time.sleep(1)
        duration -= 1

# ---------- OOP ----------
class PomodoroTimer:
    def __init__(self, work=25, break_time=5):
        self.work_duration = work * 60
        self.break_duration = break_time * 60
        self.sessions = []

    @notify
    def start_work_session(self):
        print("\n🍅 Work session started!")
        for remaining in countdown_generator(self.work_duration):
            print("⏳", remaining, end="\r")
        self.sessions.append({"type": "work", "duration": self.work_duration})
        self.save_session()

    @notify
    def start_break_session(self):
        print("\n🛌 Break session started!")
        for remaining in countdown_generator(self.break_duration):
            print("⏳", remaining, end="\r")
        self.sessions.append({"type": "break", "duration": self.break_duration})
        self.save_session()

    # ---------- File Handling ----------
    def save_session(self):
        try:
            with open("pomodoro_sessions.json", "w") as file:
                json.dump(self.sessions, file, indent=4)
        except Exception as e:
            print("Error saving session:", e)

# ---------- Usage ----------
if __name__ == "__main__":
    try:
        work_time = int(input("Enter work time (minutes): "))
        break_time = int(input("Enter break time (minutes): "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        exit()

    timer = PomodoroTimer(work_time, break_time)

    while True:
        timer.start_work_session()
        timer.start_break_session()
        cont = input("Start another Pomodoro session? (y/n): ")
        if cont.lower() != 'y':
            break

    print("\n📒 All sessions saved in 'pomodoro_sessions.json'")
