s = "Abracadabra Hocus Pocus you're a turtle dove"

# Is there a lowercase letter t in the string s?
print("t" in s)

# Is there an uppercase letter T in the string s?
print("T" in s)

# is there no uppercase letter T in s?
print("T" not in s)

# Print 15 hyphens in a row
print("-" * 15)

# Print first character in string s
print(s[0])

# Print characters 33 - 39 from string s
print(s[33:39])

# Print every third character in s starting at zero
print(s[0:44:3])

# Print the lowest character in s (a space is lower than the letter a)
print(min(s))

# Print the highest character in s
print(max(s))

# Where is the first uppercase P?
print(s.index("P"))

# Where os the first lowercase 0 in the latter half of the string s
# Note that the returned value still starts counting from zero
print(s.index("o", 22, 44))

# How many lowercase letters a are in the string s?
print(s.count("a"))

