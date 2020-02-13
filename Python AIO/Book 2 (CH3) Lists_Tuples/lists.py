students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(students[0])

print("Looping through a list")

scores = [88, 92, 78, 90, 84]
for score in scores:
	print(score)
print("Done")

# Is Anita in the list?
has_anita = "Anita" in students
print(f"Is Anita in the list? {has_anita}")

# Is Bob in the list?
has_bob = "Bob" in students
print(f"Is Bob in the list? {has_bob}")

print(f"Number of students in the list: {len(students)}")

# Add the name Goober to the list
students.append("Goober")

new_student = "Amanda"
# Add whatever name is in the new_student to the list.
if new_student in students:
	print(new_student + " already in the list")
else:
	students.append(new_student)
	print(new_student + " added to the list")

# Print the entire list
print(students)

student_name = "Lupe"

# Add student to the front of the list.
students.insert(0, student_name)

print(students)

# Changing a value
students[3] = "Hobart"

print(students)

# Extending a list
print("Extending a list...")

list1 = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba"]

# Add list2 names to list1.
list1.extend(list2)

# Print list 1.
print(list1)

# Removing items from a list
print("Removing items from a list...")

letters = ["A", "B", "C", "D", "C", "E", "C"]

# Remove "C" from the list.
letters.remove("C")

# Show me the list.
print(letters)


