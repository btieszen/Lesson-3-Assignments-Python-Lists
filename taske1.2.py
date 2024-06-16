#Python List Transformation
#Calculate the average grade and display it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print ("The Grades are:")
print(grades)
print("The average grade is:")
count = len(grades)
total = sum(grades)
average_grades = total // count
print (average_grades)