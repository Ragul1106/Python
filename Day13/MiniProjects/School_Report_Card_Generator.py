# Person Base Class
class Person:
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

    def __str__(self):
        return f"{self.name} (ID: {self.id_no})"

# Subject Class
class Subject:
    def __init__(self, name):
        self.name = name
        self.__marks = {}  # student_id → marks

    def update_marks(self, student_id, marks):
        self.__marks[student_id] = marks

    def get_marks(self, student_id):
        return self.__marks.get(student_id, "Not Graded")

    def get_all_marks(self):
        return self.__marks

    def __str__(self):
        return self.name

# Teacher Class
class Teacher(Person):
    def __init__(self, name, id_no):
        super().__init__(name, id_no)
        self.subjects = []

    def assign_subject(self, subject):
        self.subjects.append(subject)

    def update_student_marks(self, subject, student_id, marks):
        if subject in self.subjects:
            subject.update_marks(student_id, marks)
            print(f"{self.name} updated marks for student {student_id} in {subject.name}")
        else:
            print(f"{self.name} is not assigned to {subject.name}")

# Student Class
class Student(Person):
    def __init__(self, name, id_no):
        super().__init__(name, id_no)
        self.__subjects = []

    def enroll(self, subject):
        self.__subjects.append(subject)

    def get_subjects(self):
        return self.__subjects

    def get_marks(self):
        return {subj.name: subj.get_marks(self.id_no) for subj in self.__subjects}

    def __str__(self):
        return f"Student: {self.name} (ID: {self.id_no})"

# ReportCard Class
class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        print(f"\n📄 Report Card for {self.student.name}")
        marks = self.student.get_marks()
        for subject, mark in marks.items():
            grade = self.grade_system(mark)
            print(f"{subject}: {mark} → Grade: {grade}")

    def grade_system(self, marks):
        if isinstance(marks, str):
            return "Pending"
        elif marks >= 90:
            return "A+"
        elif marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "F"

"""
# Setup
math = Subject("Mathematics")
science = Subject("Science")

teacher1 = Teacher("Mrs. Latha", "T01")
teacher1.assign_subject(math)
teacher1.assign_subject(science)

student1 = Student("Vikram", "S01")
student1.enroll(math)
student1.enroll(science)

teacher1.update_student_marks(math, "S01", 85)
teacher1.update_student_marks(science, "S01", 92)

# Generate Report Card
report = ReportCard(student1)
report.generate_report()
"""