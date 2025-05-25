# Task 1: Create a Dictionary of Student Marks

try:
    students_marks = {'ohm': 78, 'jay': 87, 'prince': 98}
    name = input("Enter students name: ")
    print(name, "marks:", students_marks[name])
except KeyError:
    print("Student name not found")