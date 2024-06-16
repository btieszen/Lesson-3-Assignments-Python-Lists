#Using list methods, remove any student from the attended list who did not submit their assignment.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
p1 =set(submitted)
p2 = set(attended)
both_students =p1.intersection(p2)
new_list=set(p2) -(both_students)
print(list(new_list))
print("Have been removed from the list")
attended =[p2-new_list]
print("New attended list")
print (attended)   
        


