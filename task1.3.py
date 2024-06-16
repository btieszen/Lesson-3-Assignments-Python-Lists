#Python List Transformation
#Task 3: Replace any grade below 80 with the value Failed.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print("original grades:")
print(grades)
for i in range(len(grades)):
    if grades[i] <80:
        grades[i] = 'Failed'
print ("the new list is: ")
print(grades)
