class Course:
    def __init__(self, code, title, instructor):
        self.code = code
        self.title = title
        self.instructor = instructor
        self.students = []
        self.assignments = []
    
    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_in_course(self)
            return True
        return False
    
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
    
    def __str__(self):
        return f"{self.code}: {self.title} (Instructor: {self.instructor.name})"

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
    
    def enroll_in_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return True
        return False
    
    def submit_assignment(self, assignment, submission):
        return assignment.accept_submission(self, submission)
    
    def __str__(self):
        return f"Student {self.student_id}: {self.name}"

class Instructor:
    def __init__(self, instructor_id, name, email):
        self.instructor_id = instructor_id
        self.name = name
        self.email = email
        self.courses = []
    
    def assign_to_course(self, course):
        course.instructor = self
        self.courses.append(course)
    
    def grade_assignment(self, assignment, student, grade):
        assignment.record_grade(student, grade)
    
    def __str__(self):
        return f"Instructor {self.instructor_id}: {self.name}"

class Assignment:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.submissions = {}
        self.grades = {}
    
    def accept_submission(self, student, submission):
        self.submissions[student.student_id] = submission
        return True
    
    def record_grade(self, student, grade):
        self.grades[student.student_id] = grade
    
    def __str__(self):
        return f"Assignment: {self.title} (Due: {self.due_date})"

class CodingAssignment(Assignment):
    def accept_submission(self, student, code):

        if isinstance(code, str) and len(code) > 10:
            return super().accept_submission(student, code)
        return False

class EssayAssignment(Assignment):
    def accept_submission(self, student, essay):

        if isinstance(essay, str) and len(essay) > 500:
            return super().accept_submission(student, essay)
        return False