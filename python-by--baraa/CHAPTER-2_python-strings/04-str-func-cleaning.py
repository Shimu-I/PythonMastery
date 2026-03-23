

print("=" * 20)
print("Part 1: Cleaning WithSpaces")

text = " Engineering".lstrip()
print(text)

text1 = " Engineering"
print(text.lstrip())

text = "Engineering ".rstrip()
print(text)

text = " Engineering ".strip() # Best practice
print(text)

text = "Data Engineering".strip()
print(text) # strip() does not remvoe spaecs form the middle

text = "###Abc###".strip("#")
print(text)

# detect extra spaces
text = "   Engineering"
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())

print("Nr of spaces:", nr_of_spaces)
print("Is my data clean?", is_clean)


print("=" * 20)
print("Part 2: Case Conversions")

text = "python PROGRAMMING"
print(text.lower())
print(text.upper())


search = "Email ".lower().strip()
data = " emAil".lower().strip()

print(search == data)


 

