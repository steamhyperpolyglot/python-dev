# Create a list of strings.
letters = ["A", "B", "C", "D", "E", "F", "G"]

# Make a copy of first list item then remove it from the list.
first_removed = letters.pop(0)

last_removed = letters.pop()

# Show the new list.
print(letters)
# Show what's been removed.
print(first_removed + " and " + last_removed +
      " were removed from the list.")