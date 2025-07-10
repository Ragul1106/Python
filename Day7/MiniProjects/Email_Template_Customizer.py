name = input("Enter name: ")
course = input("Enter course: ")
duration = input("Enter duration: ")

template = "Dear {}, your {} course starts in {} days.".format(name, course, duration)
print(template)


print(f"Dear {name}, your {course} course starts in {duration} days.")