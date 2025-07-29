from icalendar import Calendar, Event as iCalEvent
from datetime import datetime, timedelta
import uuid
import os
import pickle

class Event:
    def __init__(self, title, start_time, end_time):
        self.id = str(uuid.uuid4())
        self.title = title
        self.start_time = start_time  
        self.end_time = end_time

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')})"

class CalendarScheduler:
    def __init__(self, filename="calendar.pkl"):
        self.calendar = {}  
        self.filename = filename
        self.load_calendar()

    def load_calendar(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.calendar = pickle.load(f)

    def save_calendar(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.calendar, f)

    def add_event(self, date_str, event):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            events = self.calendar.setdefault(date, [])

            for existing in events:
                if (event.start_time < existing.end_time and event.end_time > existing.start_time):
                    raise ValueError("⛔ Time conflict with another event.")

            events.append(event)
            events.sort(key=lambda e: e.start_time)
            self.save_calendar()
            print("✅ Event added successfully.")
        except ValueError as ve:
            print(f"❌ {ve}")

    def get_events_for_date(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        events = self.calendar.get(date, [])
        for event in events:
            yield event

    def export_to_ical(self, filename="schedule.ics"):
        cal = Calendar()
        for date, events in self.calendar.items():
            for e in events:
                ie = iCalEvent()
                ie.add("summary", e.title)
                ie.add("dtstart", e.start_time)
                ie.add("dtend", e.end_time)
                ie.add("uid", e.id)
                cal.add_component(ie)
        with open(filename, "wb") as f:
            f.write(cal.to_ical())
        print(f"📆 Exported to {filename}")

def main():
    scheduler = CalendarScheduler()
    while True:
        print("\n📅 Calendar Scheduler")
        print("1. Add Event")
        print("2. View Events on a Date")
        print("3. Export to iCal")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date_str = input("Enter date (YYYY-MM-DD): ")
            title = input("Enter event title: ")
            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")
            try:
                start_dt = datetime.strptime(f"{date_str} {start}", "%Y-%m-%d %H:%M")
                end_dt = datetime.strptime(f"{date_str} {end}", "%Y-%m-%d %H:%M")
                if end_dt <= start_dt:
                    raise ValueError("End time must be after start time.")
                event = Event(title, start_dt, end_dt)
                scheduler.add_event(date_str, event)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == '2':
            date_str = input("Enter date (YYYY-MM-DD): ")
            print(f"\n📆 Events on {date_str}:")
            found = False
            for e in scheduler.get_events_for_date(date_str):
                print(" -", e)
                found = True
            if not found:
                print("No events found.")

        elif choice == '3':
            scheduler.export_to_ical()

        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
