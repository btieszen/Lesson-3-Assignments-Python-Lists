#Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
new_grades=[i for i,x in enumerate(grades) if x < 80]
for item in new_grades:
    list1=students[item]
    students.remove(list1)
    students_approved=students
    print(students_approved)
    
    