# Manages available courses

available_courses = {"Math", "Science", "History", "Art"}

def list_courses():
    print("Available Courses:")
    for course in available_courses:
        print("-", course)

def is_course_available(course):
    return course in available_courses

