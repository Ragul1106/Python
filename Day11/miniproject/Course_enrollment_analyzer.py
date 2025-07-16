python_students = {'Ragul', 'Heera', 'Libi'}
java_students = {'Ranjith', 'Suba', 'Arun'}

print("Students in both:", python_students & java_students)
print("Only Python:", python_students - java_students)
print("All students:", python_students | java_students)
print("Exclusive to one course:", python_students ^ java_students)