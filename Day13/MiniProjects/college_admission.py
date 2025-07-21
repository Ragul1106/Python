class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

class Department:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_students = 0
    
    def allocate_student(self):
        if self.current_students < self.capacity:
            self.current_students += 1
            return True
        return False
    
    def __str__(self):
        return f"{self.name} Department (Capacity: {self.capacity}, Current: {self.current_students})"

class AdmissionForm:
    def __init__(self, person, documents):
        self.person = person
        self.documents = documents
        self.verified = False
    
    def verify_documents(self):
        self.verified = len(self.documents) >= 3
        return self.verified

class Student(Person):
    def __init__(self, person, admission_form, department=None):
        super().__init__(person.name, person.age, person.contact)
        self.admission_form = admission_form
        self.department = department
        self.student_id = self.generate_id()
    
    def generate_id(self):
        import random
        return f"STU{random.randint(1000, 9999)}"
    
    def allocate_department(self, department):
        if department.allocate_student():
            self.department = department
            return True
        return False
    
    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}, Department: {self.department.name if self.department else 'Not allocated'}"