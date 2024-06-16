#Advanced List Methods and Identity Operators
#Find out which students both submitted their assignments and attended the class
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
p1 =set(submitted)
p2 = set(attended)
both_students =p1.intersection(p2)
print ("Students that both submitted their assignments and attended the class")
print(both_students)




