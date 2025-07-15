registrations = {}

def register(student, course):
    registrations.setdefault(student, []).append(course)

def course_students(course):
    return [s for s, courses in registrations.items() 
            if course in courses]

register("Ragul", "CS101")
print("CS101 students:", course_students("CS101"))