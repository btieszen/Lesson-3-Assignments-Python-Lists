#Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print("The reverse order is")
temperatures.reverse()
print(temperatures)
print("The 5th to 10th day temperatures are")
segment=temperatures[5:11]
print(segment)


