#Check if the two lists are identical in terms of their content, regardless of order.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted.sort()
attended.sort()
if (submitted) == (attended):
    print ("The list are identical")
else:
    print("The list are not identical")
    
    