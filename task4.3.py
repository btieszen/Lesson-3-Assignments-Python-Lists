#print students_approved
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
new_grades=[i for i,x in enumerate(grades) if x < 80]
for item in new_grades:
    list1=students[item]
    students.remove(list1)
    students_approved=students
    students1 = '\n'.join(students_approved)
    print(students1)
    