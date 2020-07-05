# Adding and Updating List Elements

courses = ["OOP", "Networking", "MIS", "Project"]
students = ["Ahmed", "Ali", "Salim", "Abdullah", "Salwa"]
OOP_marks = [65, 85, 92]

OOP_marks.append(50)        # Add new element
OOP_marks.append(70)        # Add new element
print(OOP_marks[:])         # Print list before updating

OOP_marks[0] = 70           # update new element
OOP_marks[1] = 45           # update new element
list1 = [88, 93]
OOP_marks.extend(list1)     # extend list with another list 
print(OOP_marks[:])         # Print list after updating