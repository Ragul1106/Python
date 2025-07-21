from abc import ABC, abstractmethod

# Abstract Base Class: User
class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def show_menu(self):
        pass

# Admin class: inherits from User
class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def show_menu(self):
        print(f"Admin Menu for {self.username}")

    def create_exam(self, exam, question_text, options, correct_answer):
        question = Question(question_text, options, correct_answer)
        exam.add_question(question)
        print(f"✅ Added question to {exam.title}")

# Student class: inherits from User
class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.scores = {}

    def show_menu(self):
        print(f"Student Menu for {self.username}")

    def take_exam(self, exam):
        print(f"\n📝 {self.username} is taking the exam: {exam.title}")
        score = 0
        for i, q in enumerate(exam.questions, 1):
            print(f"\nQ{i}: {q.text}")
            for idx, option in enumerate(q.options, 1):
                print(f"{idx}. {option}")
            try:
                choice = int(input("Enter your choice (1-4): "))
                if q.check_answer(choice - 1):
                    score += 1
            except:
                print("Invalid input. Skipping question.")
        self.scores[exam.title] = score
        print(f"✅ Exam completed. Score: {score}/{len(exam.questions)}")

    def view_results(self):
        print(f"\n📊 Results for {self.username}")
        for exam, score in self.scores.items():
            print(f"{exam}: {score} marks")

# Question class with private correct answer
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.__correct_index = correct_index

    def check_answer(self, selected_index):
        return selected_index == self.__correct_index

# Exam class to hold questions
class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question: Question):
        self.questions.append(question)

"""
# Setup
admin = Admin("AdminRagul")
student = Student("Ragul123")
python_exam = Exam("Python Basics")

# Admin adds questions
admin.create_exam(python_exam, "What is the output of 2+2?", ["3", "4", "5", "6"], 1)
admin.create_exam(python_exam, "Which keyword is used to define a function?", ["fun", "def", "func", "lambda"], 1)

# Student takes the exam
student.take_exam(python_exam)

# View results
student.view_results()
"""