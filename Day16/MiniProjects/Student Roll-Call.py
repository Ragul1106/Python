class RollCall:
    def __init__(self, students):
        self.students = students
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        roll, name = list(self.students.items())[self.index]
        self.index += 1
        return (roll, name)

print("\nStudent Roll-Call:")
students = {101: "Alice", 102: "Bob", 103: "Charlie"}
for roll, name in RollCall(students):
    print(f"Roll {roll}: {name}")