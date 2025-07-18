import random

# Subjects pool
all_subjects = {"Math", "Physics", "Chemistry", "Biology", "English", "History"}

# Days and periods structure
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = [1, 2, 3, 4, 5]

def generate_timetable(timetable):
    for day in days:
        used_subjects = set()
        for period in periods:
            slot = (day, period)
            available = list(all_subjects - used_subjects)
            if not available:
                subject = random.choice(list(all_subjects))
            else:
                subject = random.choice(available)
                used_subjects.add(subject)
            timetable[slot] = subject
    print("Timetable generated successfully.")

def display_timetable(timetable):
    print("\nCollege Timetable:")
    for day in days:
        print(f"\n{day}")
        for period in periods:
            slot = (day, period)
            subject = timetable.get(slot, "Free")
            print(f"  Period {period}: {subject}")
