#Deep Dive into Python Lists
#Task 1: Given the lists:
#Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
new_grades=[i for i,x in enumerate(grades) if x < 80]
for item in new_grades:
    list1=students[item]
list2=grades[item]
list3=activities[item]
print((list1),(list2),(list3))





    













